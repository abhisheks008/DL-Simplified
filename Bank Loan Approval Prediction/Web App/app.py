import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pytorch_tabnet.tab_model import TabNetClassifier
from flask import Flask, render_template, request, redirect, url_for

# Load csv data file to get all ZIP code for a particular area
df = pd.read_csv('static/UniversalBank.csv')
zip_codes = list(df['ZIP Code'].unique().astype(str))
zip_codes.sort()

# stores predicted results
predicted_result = -1

def personal_loan(new_data):
    # Load the frequency encoding for 'ZIP Code'
    zip_code_freq = joblib.load('saved_models/zip_code_freq_encoder.pkl')

    # Load the label encoders
    label_encoders = joblib.load('saved_models/label_encoders.pkl')

    tb_cls = TabNetClassifier()
    tb_cls.load_model('saved_models/best_model.zip')

    # Apply the same frequency encoding to 'ZIP Code'
    new_data['ZIP Code'] = new_data['ZIP Code'].map(zip_code_freq)

    # Apply the same label encoding to other columns
    columns_to_encode = ['Education', 'CD Account', 'Online', 'CreditCard', 'Securities Account']
    for col in columns_to_encode:
        le = label_encoders[col]
        new_data[col] = le.transform(new_data[col])

    # Convert the DataFrame to numpy array
    new_data = new_data.to_numpy()

    # Make predictions using the loaded model
    predictions = tb_cls.predict(new_data)

    # If you need probabilities instead of class labels
    probabilities = tb_cls.predict_proba(new_data)
    
    # return predictions - either 0: rejected or 1: approved
    return [predictions, probabilities]


app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global predicted_result # global variable to get the prediction result
    
    prediction_Result = predicted_result[0][0] # stores predicted value (0 or 1)
    probability = str(predicted_result[1][0]) # stores probability of 0 and 1
    
    accuracy = probability[1:-1].split()
    rounded_numbers = [round(float(num), 3) for num in accuracy] # getting array of probabilities
    
    probability_0 = round(rounded_numbers[0]*100, 2)  # probability value for 0
    probability_1 = round(rounded_numbers[1]*100, 2)  # probability value for 1
    
    result = 'Approved' if prediction_Result == True else 'Rejected'
    
    return render_template('predict.html', result = result, probability_0=probability_0, probability_1=probability_1)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    global predicted_result
    
    # education levels displayed to users
    education_levels = [
        {'label': 'Bachelors', 'value': '1'},
        {'label': 'Masters', 'value': '2'},
        {'label': 'Advanced Degree', 'value': '3'}
    ]

    if request.method == 'POST':
        
        # Calculate age and experience difference to check conditions
        age = int(request.form['age'])
        exp = int(request.form['exp'])
        age_exp_diff = age - exp
        
        # Check if age and experience difference is less than or equal to 18
        if age_exp_diff <= 18:
            alert_message = "Your age and experience difference is less than or equal to 18."
        else:
            alert_message = None
        
        if alert_message:
            return render_template('index.html', education_levels=education_levels, zip_codes=zip_codes, alert_message=alert_message)
        
        # Check for matching education level with age
        education = int(request.form['education'])
        if education == 1:  # Bachelors
            if age < 18:
                alert_message = "Your age is not within the expected range for a Bachelors degree."
        elif education == 2:  # Masters
            if age < 21:
                alert_message = "Your age is not within the expected range for a Masters degree."
        elif education == 3:  # Advanced Degree
            if age < 23:
                alert_message = "Your age is not within the expected range for an Advanced degree."
        
        if alert_message:
            return render_template('index.html', education_levels=education_levels, zip_codes=zip_codes, alert_message=alert_message)
        
        # Retrieve form data
        # set it to boolean values for predictions
        securityAcc = int(request.form['securityAccount'])
        securityAcc = True if securityAcc == 1 else False

        cd = int(request.form['CD'])
        cd = True if cd == 1 else False

        online = int(request.form['OnlineBanking'])
        online = True if online == 1 else False

        creditCard = int(request.form['CreditCard'])
        creditCard = True if creditCard == 1 else False

        form_data = {
            'Age': [int(request.form['age'])],  # Convert to int
            'Experience': [int(request.form['exp'])],  # Convert to int
            'Income': [int(request.form['income'])],  # Convert to int
            'ZIP Code': [str(request.form['zip'])], # string
            'Family': [int(request.form['family'])],  # Convert to int
            'CCAvg': [float(request.form['cc'])],  # Convert to float
            'Education': [str(request.form['education'])],
            'Mortgage': [float(request.form['mortage'])],  # Convert to float
            'Securities Account': [securityAcc], # boolean value
            'CD Account': [cd], # boolean value
            'Online': [online], # boolean value
            'CreditCard': [creditCard] # boolean value
        }
        
        form_data = pd.DataFrame(form_data) # create dataframe
        predicted_result = personal_loan(form_data) # call function
        return redirect(url_for('predict')) # redirect to predict

    return render_template('index.html', education_levels=education_levels, zip_codes=zip_codes)


if __name__ == '__main__':
    app.run(debug=True, port=8000)

