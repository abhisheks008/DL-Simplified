param(
    [string]$Output = (Join-Path $PSScriptRoot "..\project-catalog.json"),
    [switch]$Markdown
)

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

function Get-ProjectNames {
    $commands = @(
        @("ls-tree", "-d", "--name-only", "HEAD"),
        @("ls-tree", "-d", "--name-only", "origin/main")
    )

    foreach ($command in $commands) {
        try {
            $output = & git @command 2>$null
            if ($LASTEXITCODE -eq 0 -and $output) {
                return @($output | ForEach-Object { $_.Trim() } | Where-Object {
                    $_ -and $_ -notin @(".git", ".github", "scripts")
                })
            }
        } catch {
            continue
        }
    }

    return @(Get-ChildItem -Path $repoRoot -Directory | Where-Object {
        $_.Name -notin @(".git", ".github", "scripts")
    } | ForEach-Object { $_.Name } | Sort-Object)
}

function Normalize-Name {
    param([string]$Name)
    return ($Name.ToLower() -replace '\s+', ' ').Trim()
}

$domainRules = @(
    @{
        Name = "Medical Imaging"
        Hints = @(
            "medical", "x-ray", "x ray", "xray", "ct scan", "mri", "tumor",
            "cancer", "brain", "kidney", "diabetes", "alzheimer", "malaria",
            "pneumonia", "fracture", "polyp", "cataract", "retina", "eye disease",
            "skin disease", "heart disease", "leukaemia", "leukemia", "covid",
            "monkeypox", "blood disease", "chest x-ray"
        )
    },
    @{
        Name = "Recommendation Systems"
        Hints = @("recommendation", "recommender", "recommend", "market basket", "basket", "book recommendation", "movie", "product", "sephora", "myntra", "rating")
    },
    @{
        Name = "NLP"
        Hints = @("nlp", "text", "sentiment", "tweet", "tweets", "review", "spam", "chatgpt", "resume", "essay", "topic", "author", "comment", "answers", "language", "fake news", "poem")
    },
    @{
        Name = "Time Series"
        Hints = @("time series", "stock", "weather", "sales", "forecast", "prediction", "earthquake", "cyclone", "anomaly", "traffic accident", "price", "signal", "trend")
    },
    @{
        Name = "Audio/Speech"
        Hints = @("audio", "speech", "sound", "voice", "music", "instrument", "ecg", "heartbeat", "drowsiness", "song")
    },
    @{
        Name = "Reinforcement Learning"
        Hints = @("reinforcement learning", "reinforcement", "rl", "navigation")
    },
    @{
        Name = "GANs"
        Hints = @("gan", "deepfake", "generative")
    },
    @{
        Name = "Computer Vision"
        Hints = @("image", "vision", "detection", "classif", "segmentation", "face", "object", "ocr", "captcha", "landmark", "pose", "mask", "drone", "roadmark", "animal", "fruits", "leaf", "plant", "bird", "shoe", "car", "traffic sign", "handwriting", "gesture")
    }
)

$advancedHints = @("reinforcement", "gan", "deepfake", "anomaly", "segmentation", "medical", "ct scan", "x-ray", "x ray", "mri", "navigation", "yolo", "ocr", "object detection", "multi", "generative")
$beginnerHints = @("classification", "sentiment", "spam", "analysis", "book recommendation", "review", "predictor", "prediction", "weather", "flowers", "image classification")

function Get-Domain {
    param([string]$Project)

    $text = Normalize-Name $Project
    foreach ($rule in $domainRules) {
        foreach ($hint in $rule.Hints) {
            if ($text -like "*$hint*") {
                return $rule.Name
            }
        }
    }

    return "Other / Tabular"
}

function Get-Difficulty {
    param(
        [string]$Project,
        [string]$Domain
    )

    $text = Normalize-Name $Project

    foreach ($hint in $advancedHints) {
        if ($text -like "*$hint*") {
            return "Advanced"
        }
    }

    if ($Domain -eq "Medical Imaging" -and ($text -match "detection|segmentation|classification")) {
        return "Advanced"
    }

    if ($Domain -eq "Reinforcement Learning" -or $Domain -eq "GANs") {
        return "Advanced"
    }

    foreach ($hint in $beginnerHints) {
        if ($text -like "*$hint*") {
            return "Beginner"
        }
    }

    if ($Domain -in @("Computer Vision", "NLP", "Recommendation Systems", "Audio/Speech")) {
        return "Intermediate"
    }

    if ($Domain -eq "Other / Tabular") {
        if ($text -like "*prediction*") {
            return "Intermediate"
        }

        return "Beginner"
    }

    return "Intermediate"
}

$projects = Get-ProjectNames
$catalog = foreach ($project in $projects | Sort-Object) {
    $domain = Get-Domain $project
    $difficulty = Get-Difficulty -Project $project -Domain $domain

    [PSCustomObject]@{
        project = $project
        path = $project
        domain = $domain
        difficulty = $difficulty
    }
}

$json = $catalog | ConvertTo-Json -Depth 4
[System.IO.File]::WriteAllText($Output, $json + [Environment]::NewLine, [System.Text.Encoding]::UTF8)

if ($Markdown) {
    $domainGroups = $catalog | Group-Object domain | Sort-Object Name
    $difficultyOrder = @("Beginner", "Intermediate", "Advanced")
    $difficultyGroups = $catalog | Group-Object difficulty

    Write-Output "## Project Catalog"
    Write-Output ""
    Write-Output "### By Domain"
    Write-Output ""
    Write-Output "| Domain | Count | Sample projects |"
    Write-Output "| --- | ---: | --- |"
    foreach ($group in $domainGroups) {
        $samples = ($group.Group | Select-Object -First 3 | ForEach-Object { $_.project }) -join ", "
        Write-Output ("| {0} | {1} | {2} |" -f $group.Name, $group.Count, $samples)
    }

    Write-Output ""
    Write-Output "### By Difficulty"
    Write-Output ""
    Write-Output "| Difficulty | Count |"
    Write-Output "| --- | ---: |"
    foreach ($difficulty in $difficultyOrder) {
        $count = ($difficultyGroups | Where-Object { $_.Name -eq $difficulty } | Select-Object -ExpandProperty Count)
        if (-not $count) { $count = 0 }
        Write-Output ("| {0} | {1} |" -f $difficulty, $count)
    }

    Write-Output ""
    Write-Output "### Source"
    Write-Output ""
    Write-Output "- `project-catalog.json` is the source of truth for the generated catalog."
    Write-Output "- Rebuild it with `powershell -ExecutionPolicy Bypass -File scripts/generate_project_catalog.ps1 -Markdown`."
}
