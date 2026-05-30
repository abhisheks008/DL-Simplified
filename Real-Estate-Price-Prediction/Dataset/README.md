# Dataset: Bengaluru House Price Data

## Source
[Kaggle - Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)

## Description
This dataset contains real estate listing information from Bengaluru, India, with features that influence housing prices.

## Columns
| Column | Description |
|--------|-------------|
| `area_type` | Type of area (Super built-up, Built-up, Plot, Carpet) |
| `availability` | Possession status (Ready to Move / specific date) |
| `location` | Locality in Bengaluru |
| `size` | Number of BHK/Bedrooms (e.g., "2 BHK", "3 Bedroom") |
| `society` | Name of the housing society (if applicable) |
| `total_sqft` | Total square footage of the property |
| `bath` | Number of bathrooms |
| `balcony` | Number of balconies |
| `price` | Price in Lakhs (INR) |

## Preprocessing Notes
- `size` column needs parsing to extract numeric BHK count
- `total_sqft` may contain ranges (e.g., "2000-2500") — use midpoint
- Missing values present in `bath`, `balcony`, `society`
- Outliers in `price_per_sqft` removed using std deviation logic per location
- `location` has high cardinality — rare locations grouped as "other" before OHE

## Download Instructions
1. Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
2. Download `Bengaluru_House_Data.csv`
3. Place it in this `Dataset/` folder
