
# resume_analyzer.py

import os
import re
import logging
import fitz  # PyMuPDF for PDF text extraction
from rapidfuzz import fuzz
from typing import List, Dict, Tuple
from datetime import datetime
import tempfile
from fpdf import FPDF
from sentence_transformers import util
import utils  # Import the utils module

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

class ResumeAnalyzer:
    def __init__(self):
        self.nlp = utils.load_nlp_model()
        self.model = utils.load_transformer_model()
        self.SKILL_KEYWORDS = self._load_skill_keywords()
        self.JOB_TITLES = list(self.SKILL_KEYWORDS.keys())

    def _load_skill_keywords(self) -> Dict[str, List[str]]:
        return {
            "Data Scientist": [
                "Python", "R", "SQL", "Pandas", "NumPy", "Scikit-learn",
                "TensorFlow", "PyTorch", "Tableau", "Power BI", "Machine Learning",
                "Deep Learning", "Natural Language Processing", "Data Analysis",
                "Data Visualization", "Statistics", "Predictive Modeling", "Big Data"
            ],
            "Software Engineer": [
                "Java", "C++", "C#", "Python", "JavaScript", "Git", "Agile Methodologies",
                "Unit Testing", "OOP", "REST APIs", "Microservices", "SQL", "NoSQL",
                "Linux", "Docker", "Kubernetes", "Design Patterns", "Algorithms", "Data Structures"
            ],
            "Web Developer": [
                "HTML", "CSS", "JavaScript", "React", "Angular", "Vue.js",
                "Node.js", "Django", "Flask", "Ruby on Rails", "Bootstrap",
                "jQuery", "Webpack", "REST APIs", "GraphQL", "TypeScript", "Responsive Design", "SEO"
            ],
            "Mobile App Developer": [
                "Swift", "Kotlin", "React Native", "Flutter", "Android Studio",
                "Xcode", "Firebase", "UI/UX Design", "Mobile Security", "Objective-C",
                "Java", "Dart", "APIs", "Cross-Platform Development", "SQLite", "JSON"
            ],
            "DevOps Engineer": [
                "Git", "Docker", "Kubernetes", "Terraform", "Ansible",
                "AWS", "Azure", "GCP", "Jenkins", "CI/CD", "Monitoring", "Logging",
                "Bash", "PowerShell", "Prometheus", "Grafana", "Infrastructure as Code", "Scripting", "Linux"
            ],
            "Cybersecurity Specialist": [
                "Network Security", "Information Security", "Penetration Testing", "Vulnerability Assessment",
                "Ethical Hacking", "Firewalls", "Intrusion Detection", "Incident Response",
                "Security Compliance", "Encryption", "Risk Management", "SIEM", "IDS/IPS", "Security Auditing"
            ],
            "Database Administrator": [
                "SQL", "NoSQL", "Oracle", "MySQL", "PostgreSQL", "MongoDB", "Database Design",
                "Data Modeling", "Performance Tuning", "Backup and Recovery", "PL/SQL",
                "Data Warehousing", "ETL", "SQL Server", "Replication"
            ],
            "Cloud Architect": [
                "AWS", "Azure", "GCP", "Cloud Computing", "Cloud Infrastructure",
                "Cloud Security", "DevOps", "Docker", "Kubernetes", "Automation",
                "CI/CD", "IaaS", "PaaS", "SaaS", "Virtualization", "Disaster Recovery"
            ],
            "AI Researcher": [
                "Machine Learning", "Deep Learning", "Python", "TensorFlow", "PyTorch",
                "Natural Language Processing", "Computer Vision", "Reinforcement Learning",
                "Algorithms", "Research", "Mathematics", "Statistics", "C++", "Data Analysis", "Artificial Intelligence"
            ],
            "Data Engineer": [
                "Python", "Scala", "Java", "SQL", "NoSQL", "ETL", "Hadoop", "Spark",
                "Kafka", "Airflow", "Data Warehousing", "Big Data", "AWS", "Azure",
                "Data Pipelines", "Data Modeling", "Redshift", "Snowflake"
            ],
            "Network Engineer": [
                "Networking", "Cisco", "Juniper", "TCP/IP", "Routing", "Switching",
                "Network Security", "Firewalls", "VPN", "LAN/WAN", "Wireless Networks",
                "Network Troubleshooting", "VoIP", "BGP", "OSPF", "Network Monitoring"
            ],
            "Business Analyst": [
                "Business Analysis", "Requirements Gathering", "SQL", "Data Analysis",
                "Process Modeling", "UML", "Agile Methodologies", "User Stories",
                "Project Management", "Communication Skills", "Microsoft Excel",
                "Stakeholder Management", "JIRA", "Confluence"
            ],
            "Project Manager": [
                "Project Management", "Agile", "Scrum", "Kanban", "Risk Management",
                "Budgeting", "Scheduling", "Communication Skills", "Leadership",
                "Microsoft Project", "Stakeholder Management", "Team Management", "PMP Certification"
            ],
            "UX/UI Designer": [
                "User Experience", "User Interface", "Adobe XD", "Sketch", "Figma",
                "Wireframing", "Prototyping", "User Research", "Interaction Design",
                "Visual Design", "HTML", "CSS", "Usability Testing", "Adobe Creative Suite"
            ],
            "Quality Assurance Engineer": [
                "Quality Assurance", "Testing", "Test Automation", "Selenium", "JUnit",
                "Test Cases", "Bug Tracking", "Regression Testing", "Performance Testing",
                "Load Testing", "Agile Methodologies", "QA Processes", "Cucumber", "TestNG"
            ],
            "Systems Analyst": [
                "Systems Analysis", "Requirements Analysis", "Business Analysis",
                "SQL", "Data Modeling", "Process Improvement", "Technical Documentation",
                "Software Development Life Cycle", "UML", "Testing", "Problem-Solving", "ERP Systems"
            ],
            "Software Tester": [
                "Software Testing", "Manual Testing", "Automated Testing", "Test Cases",
                "Selenium", "LoadRunner", "Bug Tracking", "Quality Assurance",
                "Regression Testing", "Test Plans", "Agile Testing", "Black Box Testing", "White Box Testing"
            ],
            "Technical Writer": [
                "Technical Writing", "Documentation", "Writing Skills", "API Documentation",
                "User Manuals", "Microsoft Office", "Adobe Acrobat", "Content Management",
                "Editing", "Communication Skills", "XML", "Markdown", "DITA"
            ],
            "Sales Engineer": [
                "Sales", "Technical Knowledge", "Product Demonstrations", "Client Relations",
                "Negotiation Skills", "Communication Skills", "CRM Software", "Presentations",
                "Solution Selling", "Technical Support", "B2B Sales", "Networking"
            ],
            "IT Support Specialist": [
                "Technical Support", "Troubleshooting", "Windows OS", "Mac OS", "Linux",
                "Hardware Support", "Software Installation", "Network Support",
                "Customer Service", "Active Directory", "Help Desk", "Ticketing Systems"
            ],
            "Machine Learning Engineer": [
                "Python", "TensorFlow", "PyTorch", "Scikit-learn", "Machine Learning",
                "Deep Learning", "Algorithms", "Data Structures", "Data Preprocessing",
                "Model Deployment", "AWS SageMaker", "Big Data", "Distributed Computing", "MLOps"
            ],
            "Full Stack Developer": [
                "JavaScript", "Python", "Ruby", "Java", "Node.js", "React", "Angular",
                "Vue.js", "Django", "Flask", "Ruby on Rails", "SQL", "NoSQL", "REST APIs",
                "GraphQL", "HTML", "CSS", "Webpack", "Microservices", "TypeScript"
            ],
            "Product Manager": [
                "Product Management", "Roadmapping", "Agile Methodologies", "Scrum",
                "Market Research", "User Experience", "Project Management", "Stakeholder Management",
                "Communication Skills", "Data Analysis", "Prioritization", "Product Lifecycle"
            ],
            "Data Analyst": [
                "SQL", "Excel", "Python", "R", "Tableau", "Power BI", "Data Visualization",
                "Statistics", "Data Mining", "Data Cleaning", "Business Intelligence",
                "Data Modeling", "Analytics", "SAS", "SPSS"
            ],
            "Embedded Systems Engineer": [
                "C", "C++", "Microcontrollers", "Firmware", "RTOS", "Embedded Linux",
                "Hardware Design", "Debugging", "IoT", "Circuit Design", "Assembly Language",
                "Sensors", "Protocols (I2C, SPI, UART)", "VHDL", "Verilog"
            ],
            "Systems Engineer": [
                "Systems Engineering", "Linux", "Windows Server", "Scripting",
                "Automation", "Ansible", "Puppet", "Docker", "Virtualization",
                "Cloud Computing", "Networking", "Troubleshooting", "Active Directory"
            ],
            "SEO Specialist": [
                "SEO", "Google Analytics", "Keyword Research", "Content Optimization",
                "HTML", "CSS", "Link Building", "On-page Optimization", "Off-page Optimization",
                "SEM", "Marketing", "Digital Analytics", "Google Search Console"
            ],
            "Graphic Designer": [
                "Adobe Photoshop", "Adobe Illustrator", "InDesign", "Graphic Design",
                "Branding", "Typography", "Layout Design", "Color Theory",
                "Creative Suite", "Sketch", "Visual Communication", "After Effects", "3D Modeling"
            ],
            "Content Writer": [
                "Content Writing", "SEO", "Blogging", "Copywriting", "Editing",
                "Proofreading", "Research", "Social Media", "Marketing", "WordPress",
                "Creative Writing", "Content Strategy"
            ],
            "Blockchain Developer": [
                "Blockchain", "Ethereum", "Solidity", "Smart Contracts", "Cryptocurrency",
                "Bitcoin", "Hyperledger", "Web3.js", "Cryptography", "Distributed Ledger",
                "Consensus Algorithms", "Truffle", "Ganache"
            ],
            "Artificial Intelligence Engineer": [
                "Artificial Intelligence", "Machine Learning", "Deep Learning",
                "Python", "TensorFlow", "PyTorch", "NLP", "Computer Vision",
                "Reinforcement Learning", "Algorithms", "Data Structures", "Keras", "OpenCV"
            ]
        }

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        try:
            with fitz.open(pdf_path) as pdf_document:
                text = "\n".join(page.get_text("text") for page in pdf_document)
                return text.strip()
        except Exception as e:
            logging.error(f"PDF extraction error for {pdf_path}: {e}")
            return ""

    def preprocess_text(self, text: str) -> str:
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)
        return text.strip()

    def extract_job_title_and_primary_skills(self, job_description: str) -> Tuple[List[str], List[str]]:
        doc = self.nlp(job_description)
        job_description_lower = job_description.lower()
        extracted_titles = []
        for title in self.JOB_TITLES:
            if title.lower() in job_description_lower:
                extracted_titles.append(title)
        extracted_skills = set()
        for token in doc:
            for skills in self.SKILL_KEYWORDS.values():
                if token.text in skills:
                    extracted_skills.add(token.text)
        for entity in doc.ents:
            for skills in self.SKILL_KEYWORDS.values():
                if entity.text in skills:
                    extracted_skills.add(entity.text)
        return extracted_titles, list(extracted_skills)

    def extract_all_skills(self, resume_text: str) -> List[str]:
        doc = self.nlp(resume_text)
        extracted_skills = set()
        for token in doc:
            for skills in self.SKILL_KEYWORDS.values():
                if token.text in skills:
                    extracted_skills.add(token.text)
        for entity in doc.ents:
            for skills in self.SKILL_KEYWORDS.values():
                if entity.text in skills:
                    extracted_skills.add(entity.text)
        return list(extracted_skills)

    def match_primary_skills(self, resume_skills: List[str], job_description_skills: List[str]) -> List[str]:
        return list(set(resume_skills) & set(job_description_skills))

    def extract_secondary_skills(self, resume_skills: List[str], primary_skills: List[str], job_titles: List[str]) -> List[str]:
        secondary_skills = set()
        for title in job_titles:
            if title in self.SKILL_KEYWORDS:
                title_skills = set(self.SKILL_KEYWORDS[title])
                additional_skills = (title_skills & set(resume_skills)) - set(primary_skills)
                secondary_skills.update(additional_skills)
        return list(secondary_skills)

    def extract_project_section(self, resume_text: str) -> str:
        headings = ['Projects', 'Project Experience', 'Relevant Projects', 'Academic Projects', 'Professional Projects']
        pattern = r'(?i)(' + '|'.join(headings) + r')\b'
        match = re.search(pattern, resume_text)
        if match:
            start = match.end()
            end_match = re.search(r'\n[A-Z][^\n]+\n', resume_text[start:])
            end = start + end_match.start() if end_match else len(resume_text)
            project_section = resume_text[start:end].strip()
            return project_section
        return ''

    def extract_project_skills(self, project_section: str) -> List[str]:
        doc = self.nlp(project_section)
        project_skills = set()
        for token in doc:
            if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
                project_skills.add(token.text)
        for chunk in doc.noun_chunks:
            project_skills.add(chunk.text.strip())
        return list(project_skills)

    def extract_advanced_terms(self, job_description: str) -> List[str]:
        doc = self.nlp(job_description)
        advanced_terms = set()
        for chunk in doc.noun_chunks:
            text = chunk.text.strip()
            if len(text.split()) > 1 and not text.lower().startswith(('we are', 'the candidate', 'you will')):
                advanced_terms.add(text)
        return list(advanced_terms)

    def assess_project_relevance(self, project_skills: List[str], required_skills: List[str], advanced_terms: List[str]) -> float:
        matched_skills = set()
        for skill in required_skills:
            for project_skill in project_skills:
                if fuzz.partial_ratio(skill.lower(), project_skill.lower()) > 80:
                    matched_skills.add(skill)
                    break
        skill_relevance = len(matched_skills) / len(required_skills) if required_skills else 0
        complexity = 0
        for term in advanced_terms:
            for project_skill in project_skills:
                if fuzz.partial_ratio(term.lower(), project_skill.lower()) > 80:
                    complexity += 1
                    break
        complexity_score = complexity / len(advanced_terms) if advanced_terms else 0
        relevance_score = (skill_relevance * 0.8) + (complexity_score * 0.2)
        return relevance_score

    def analyze_projects(self, resume_text: str, job_description: str, required_skills: List[str]) -> Tuple[int, float]:
        advanced_terms = self.extract_advanced_terms(job_description)
        project_section = self.extract_project_section(resume_text)
        if not project_section:
            logging.info("No project section found in resume.")
            return 0, 0.0
        project_skills = self.extract_project_skills(project_section)
        relevance_score = self.assess_project_relevance(project_skills, required_skills, advanced_terms)
        relevant_project_count = 1 if relevance_score > 0.2 else 0
        average_relevance_score = relevance_score if relevant_project_count else 0.0
        return relevant_project_count, average_relevance_score

    def extract_experience_section(self, resume_text: str) -> str:
        headings = [
            'Work Experience', 'Professional Experience', 'Employment History',
            'Experience', 'Relevant Experience', 'Internship Experience', 'Internships'
        ]
        pattern = r'(?i)(' + '|'.join(headings) + r')\b'
        match = re.search(pattern, resume_text)
        if match:
            start = match.end()
            end_match = re.search(r'\n[A-Z][^\n]+\n', resume_text[start:])
            end = start + end_match.start() if end_match else len(resume_text)
            experience_section = resume_text[start:end].strip()
            return experience_section
        return ''

    def parse_individual_experiences(self, experience_section: str) -> List[Dict[str, str]]:
        entries = re.split(r'\n\s*\n', experience_section)
        experiences = []
        for entry in entries:
            entry = entry.strip()
            if entry:
                lines = entry.split('\n')
                job_title = lines[0].strip() if lines else ''
                company = lines[1].strip() if len(lines) > 1 else ''
                experiences.append({
                    'description': entry,
                    'job_title': job_title,
                    'company': company
                })
        return experiences

    def assess_experience_relevance(self, experience_description: str, required_skills: List[str], job_titles: List[str]) -> float:
        tokens = set(token.text.lower() for token in self.nlp(experience_description) if not token.is_stop)
        matched_skills = [skill.lower() for skill in required_skills if skill.lower() in tokens]
        skill_relevance = len(matched_skills) / len(required_skills) if required_skills else 0
        matched_titles = [title.lower() for title in job_titles if title.lower() in experience_description.lower()]
        title_relevance = 1.0 if matched_titles else 0.0
        relevance_score = (skill_relevance * 0.7) + (title_relevance * 0.3)
        return relevance_score

    def assess_experience_relevance_semantic(self, experience_description: str, job_description: str) -> float:
        embedding_experience = self.model.encode(experience_description, convert_to_tensor=True)
        embedding_job = self.model.encode(job_description, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embedding_experience, embedding_job).item()
        return similarity

    def calculate_experience_relevance(self, experience_description: str, required_skills: List[str], job_titles: List[str], job_description: str) -> float:
        relevance_keyword = self.assess_experience_relevance(experience_description, required_skills, job_titles)
        relevance_semantic = self.assess_experience_relevance_semantic(experience_description, job_description)
        relevance_score = (relevance_keyword * 0.6) + (relevance_semantic * 0.4)
        return relevance_score

    def extract_experience_duration(self, experience_description: str) -> float:
        from dateutil import parser
        date_patterns = [
            r'((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[\s\-.,]\d{2,4})',
            r'(\b\d{1,2}/\d{1,2}/\d{2,4})',
            r'(\b\d{1,2}-\d{1,2}-\d{2,4})',
            r'(\b\d{4}\b)',
            r'(\b\d{1,2}/\d{4})',
        ]
        start_date = None
        end_date = None
        matches = []
        for pattern in date_patterns:
            matches.extend(re.findall(pattern, experience_description, re.IGNORECASE))
        for match in matches:
            date_str = match[0]
            if 'present' in date_str.lower():
                end_date = datetime.now()
            else:
                try:
                    date = parser.parse(date_str, fuzzy=True)
                    if not start_date or date < start_date:
                        start_date = date
                    if not end_date or date > end_date:
                        end_date = date
                except Exception:
                    continue
        if start_date and end_date:
            duration = (end_date - start_date).days / 365.25
            return max(duration, 0)
        return 0.0

    def analyze_experience(self, resume_text: str, job_description: str, required_skills: List[str], job_titles: List[str]) -> Tuple[float, float]:
        experience_section = self.extract_experience_section(resume_text)
        if not experience_section:
            return 0.0, 0.0
        experiences = self.parse_individual_experiences(experience_section)
        relevant_experience_duration = 0.0
        total_relevance_score = 0.0
        for exp in experiences:
            exp_desc = exp['description']
            relevance_score = self.calculate_experience_relevance(exp_desc, required_skills, job_titles, job_description)
            duration = self.extract_experience_duration(exp_desc)
            relevant_experience_duration += duration * relevance_score
            total_relevance_score += relevance_score
        average_relevance_score = total_relevance_score / len(experiences) if experiences else 0.0
        return relevant_experience_duration, average_relevance_score

    def analyze_total_experience(self, resume_text: str) -> float:
        experience_years = 0.0
        patterns = [
            r'(\d+)\+?\s+years of experience',
            r'over\s+(\d+)\s+years',
            r'(\d+)\s+years\'\s+experience',
            r'experience of\s+(\d+)\s+years',
            r'(\d+)-year experience',
            r'experience\s+spanning\s+(\d+)\s+years'
        ]
        for pattern in patterns:
            matches = re.findall(pattern, resume_text, re.IGNORECASE)
            for match in matches:
                experience_years = max(experience_years, float(match))
        return experience_years

    def rank_resume(self, primary_skills: List[str], secondary_skills: List[str], total_experience: float,
                    relevant_experience_duration: float, average_experience_relevance: float,
                    relevant_project_count: int, average_project_relevance: float) -> float:
        score = 0.0
        score += len(primary_skills) * 5
        score += len(secondary_skills) * 3
        score += total_experience * 1.5
        score += relevant_experience_duration * average_experience_relevance * 5
        score += relevant_project_count * average_project_relevance * 2
        return score

    def analyze_resume(self, resume_file: str, job_description: str) -> Dict[str, any]:
        job_titles, job_description_skills = self.extract_job_title_and_primary_skills(job_description)
        if not job_titles:
            logging.warning("No job titles found in job description.")
            return {}
        required_skills = job_description_skills
        resume_text = self.extract_text_from_pdf(resume_file)
        resume_text = self.preprocess_text(resume_text)
        resume_skills = self.extract_all_skills(resume_text)
        primary_skills = self.match_primary_skills(resume_skills, required_skills)
        secondary_skills = self.extract_secondary_skills(resume_skills, primary_skills, job_titles)
        total_experience_years = self.analyze_total_experience(resume_text)
        relevant_experience_duration, average_experience_relevance = self.analyze_experience(
            resume_text, job_description, required_skills, job_titles
        )
        relevant_project_count, average_project_relevance = self.analyze_projects(
            resume_text, job_description, required_skills
        )
        score = self.rank_resume(
            primary_skills, secondary_skills, total_experience_years,
            relevant_experience_duration, average_experience_relevance,
            relevant_project_count, average_project_relevance
        )
        result = {
            "Resume Name": os.path.basename(resume_file),
            "Job Titles": job_titles,
            "Primary Skills": primary_skills,
            "Secondary Skills": secondary_skills,
            "Total Experience (Years)": total_experience_years,
            "Relevant Experience Duration (Years)": relevant_experience_duration,
            "Average Experience Relevance": average_experience_relevance,
            "Relevant Projects": relevant_project_count,
            "Average Project Relevance": average_project_relevance,
            "Score": score
        }
        return result

    def analyze_resumes(self, resume_files: List[str], job_description: str) -> List[Dict[str, any]]:
        results = []
        for resume_file in resume_files:
            result = self.analyze_resume(resume_file, job_description)
            if result:
                results.append(result)
        results.sort(key=lambda x: x['Score'], reverse=True)
        return results

    def generate_ranking_report(self, analysis_results):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Resume Analysis Report", ln=True, align="C")
        pdf.ln(10)
        for result in analysis_results:
            pdf.cell(200, 10, txt=f"Resume Name: {result['Resume Name']}", ln=True)
            pdf.cell(200, 10, txt=f"Job Titles: {', '.join(result['Job Titles'])}", ln=True)
            pdf.cell(200, 10, txt=f"Primary Skills: {', '.join(result['Primary Skills'])}", ln=True)
            pdf.cell(200, 10, txt=f"Secondary Skills: {', '.join(result['Secondary Skills'])}", ln=True)
            pdf.cell(200, 10, txt=f"Total Experience (Years): {result['Total Experience (Years)']}", ln=True)
            pdf.cell(200, 10, txt=f"Relevant Experience Duration (Years): {result['Relevant Experience Duration (Years)']:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Average Experience Relevance: {result['Average Experience Relevance']:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Relevant Projects: {result['Relevant Projects']}", ln=True)
            pdf.cell(200, 10, txt=f"Average Project Relevance: {result['Average Project Relevance']:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Score: {result['Score']:.2f}", ln=True)
            pdf.cell(200, 10, txt="-" * 50, ln=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf_output_path = tmp_file.name
            pdf.output(pdf_output_path)
        return pdf_output_path
