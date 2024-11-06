# Dataset Overview

The project uses a synthetic dataset to simulate traffic accident occurrences based on several conditions over a one-year period (365 days). This data is intended to train a deep learning model, specifically an LSTM, for predicting accidents based on historical trends.

## Dataset Structure

The dataset includes the following features:

| Feature              | Description                                                                                  | Type      |
|----------------------|----------------------------------------------------------------------------------------------|-----------|
| **Date**             | A sequence of dates over one year, used as the time basis for other data.                    | Date      |
| **Traffic Volume**   | Simulated daily traffic volume, with random values within a range (e.g., 100 to 2000).       | Integer   |
| **Weather Condition**| Categorical data representing different weather scenarios, including `clear`, `rain`, `fog`, and `snow`. | Categorical |
| **Road Type**        | Categorical data representing types of roads, such as `highway`, `urban road`, and `rural road`. | Categorical |
| **Accident Occurred**| Binary indicator of whether an accident occurred on a given day, based on traffic and weather conditions. | Binary    |

## Accident Occurrence Simulation

The likelihood of an accident is influenced by:

- **Weather Conditions**: Higher chance of accidents under `rain`, `fog`, or `snow`.
- **Traffic Volume**: Accidents become more likely with increased traffic volume, particularly above 1500 vehicles per day.

For example:
- A 30% chance of an accident occurs when traffic is high and the weather is adverse.
- A lower, 5% base chance is assigned for normal conditions.

## Example Dataset (First 5 Rows)

| Date       | Traffic Volume | Weather Condition | Road Type    | Accident Occurred |
|------------|----------------|-------------------|--------------|--------------------|
| 2023-01-01 | 1500           | Clear            | Urban road   | 0                 |
| 2023-01-02 | 1800           | Rain             | Highway      | 1                 |
| 2023-01-03 | 1300           | Fog              | Rural road   | 0                 |
| 2023-01-04 | 1900           | Snow             | Highway      | 1                 |
| 2023-01-05 | 1200           | Clear            | Urban road   | 0                 |

This structured data is used to train the LSTM model for predicting accident probabilities, with categorical features encoded and normalized for model readiness.
