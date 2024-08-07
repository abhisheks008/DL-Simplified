# Laptop Price Prediction Webapp

## Goal 🎯

The primary objective of this project is to develop a user-friendly web application tailored for accurately predicting the Market Retail Price (MRP) of laptops based on their attributes using advanced machine learning models.

## Model Used for the Web App 🧮

The web application utilizes a machine learning model trained for Laptop Price Prediction. The model architecture includes a regression model trained on a dataset of laptops with various attributes.

## Features of the Web App 🌐

- **Input Laptop Attributes**: Allows users to input 13 different attributes of a laptop.
- **MRP Prediction**: Provides the predicted MRP based on the input attributes.
- **Detailed Insights**: Offers detailed insights about how different attributes affect the MRP.

**Note:** Ensure to update the paths accordingly based on your local machine's directory structure.


# How to Use

## Requirements
1. *Python Installation*: Ensure Python is installed on your system. Streamlit requires Python 3.7 - 3.10.
2. *Streamlit Installation*: Install Streamlit and other necessary libraries. You can find the list of required packages in the requirements.txt file.

## Steps to Run

1. *Clone the Repository*
   Download the project repository containing the Streamlit application.
   ``` bash
    git clone https://github.com/abhisheks008/DL-Simplified.git
   ```

3. *Install Dependencies*
   Navigate to the project directory and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. *Download Data*
   Download any necessary datasets and place them in the specified directories as mentioned in the project documentation.

5. *Run the Streamlit Application*
   Navigate to the directory containing the Streamlit script (e.g., app.py) and run the following command:
   ```bash
   streamlit run web.py
   ```

6. *Open the Application*
   After running the above command, Streamlit will provide a local URL (usually http://localhost:8501) where you can access the application in your web browser.

## Example Commands

1. *Clone the Repository*
   bash
   git clone <repository_url>
   cd <project_directory>
   

2. *Install Dependencies*
   bash
   pip install -r requirements.txt
   

3. *Run the Streamlit Application*
   bash
   streamlit run app.py
   

4. *Open in Browser*
   Access the provided URL in your browser to interact with the Streamlit application.

By following these steps, you will be able to run the Streamlit application locally on your system. Make sure to update any file paths or configurations as needed for your environment.

## Contributing

We welcome contributions to improve this project! If you're interested in contributing, please follow these guidelines:

1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

3. **Create a Branch**: Create a new branch for your feature or bug fix. Use a descriptive name for the branch.
    ```bash
    git checkout -b feature-or-bugfix-name
    ```

4. **Make Changes**: Make your changes to the codebase. Ensure your code adheres to the project's coding standards and practices.

5. **Commit Changes**: Commit your changes with a clear and descriptive commit message.
    ```bash
    git add .
    git commit -m "Description of the feature or bug fix"
    ```

6. **Push Changes**: Push your changes to your forked repository.
    ```bash
    git push origin feature-or-bugfix-name
    ```

7. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request from your forked repository's branch. Provide a clear description of your changes and the reason for the contribution.

## Deployed Web Application

The web application is deployed using Streamlit Cloud. You can access it using the following link:

[**Laptop Price Prediction Web App**](https://laptop-price-predictor-deep-learning.streamlit.app/)

