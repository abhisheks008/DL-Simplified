# Dataset — Animals-10

## Dataset Details

| Property | Value |
|---|---|
| **Name** | Animals-10 |
| **Source** | Kaggle |
| **Link** | https://www.kaggle.com/datasets/alessiocorrado99/animals10/discussion?sort=hotness |
| **Total Images** | ~26,000 |
| **Classes** | 10 |
| **Image Format** | JPEG / PNG |
| **Image Size** | Variable (resized to 224×224 for training) |

## Classes

| Class | Italian Folder Name | Image Count (approx) |
|---|---|---|
| Dog | cane | ~2500 |
| Horse | cavallo | ~2500 |
| Elephant | elefante | ~1500 |
| Butterfly | farfalla | ~2100 |
| Chicken | gallina | ~3000 |
| Cat | gatto | ~1700 |
| Cow | mucca | ~1900 |
| Sheep | pecora | ~1600 |
| Spider | ragno | ~4700 |
| Squirrel | scoiattolo | ~1900 |

## Dataset Split

| Split | Percentage | Images |
|---|---|---|
| Train | 80% | ~20,800 |
| Validation | 10% | ~2,600 |
| Test | 10% | ~2,600 |

## Download Instructions

```bash
# Using Kaggle API
kaggle datasets download -d alessiocorrado99/animals10
unzip animals10.zip -d animals10
```

## Notes
- Dataset file is too large to upload directly (>500MB)
- Use the Kaggle link above to download
- Folder names are in Italian — notebook handles renaming automatically