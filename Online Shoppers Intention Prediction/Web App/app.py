from pathlib import Path
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
MODEL_DIR = PROJECT_DIR / 'Model'
DATA_PATH = PROJECT_DIR / 'Dataset' / 'online_shoppers_intention.csv'

MODEL_FILE = MODEL_DIR / '04_deep_network_model.h5'
SCALER_FILE = MODEL_DIR / 'feature_scaler.pkl'
ENCODERS_FILE = MODEL_DIR / 'label_encoders.pkl'
TARGET_ENCODER_FILE = MODEL_DIR / 'target_encoder.pkl'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'replace-this-with-a-secure-value'

model = load_model(str(MODEL_FILE))
scaler = pickle.load(open(SCALER_FILE, 'rb'))
label_encoders = pickle.load(open(ENCODERS_FILE, 'rb'))
target_encoder = pickle.load(open(TARGET_ENCODER_FILE, 'rb'))

MODEL_REGISTRY = {
    'MLP': load_model(str(MODEL_DIR / '01_mlp_model.h5')),
    'LSTM': load_model(str(MODEL_DIR / '02_lstm_model.h5')),
    'GRU': load_model(str(MODEL_DIR / '03_gru_model.h5')),
    'Deep Network': model,
}

def build_lookup_tables():
    months = [
        ('Aug', 'August'),
        ('Dec', 'December'),
        ('Feb', 'February'),
        ('Jul', 'July'),
        ('June', 'June'),
        ('Mar', 'March'),
        ('May', 'May'),
        ('Nov', 'November'),
        ('Oct', 'October'),
        ('Sep', 'September'),
    ]
    visitor_types = [
        ('Returning Visitor', 'Returning Visitor'),
        ('New Visitor', 'New Visitor'),
        ('Other', 'Other'),
    ]
    os_options = [(str(v), f'OS Category {v}') for v in range(1, 9)]
    browser_options = [(str(v), f'Browser Category {v}') for v in range(1, 14)]
    region_options = [(str(v), f'Region Category {v}') for v in range(1, 10)]
    traffic_options = [(str(v), f'Traffic Source Category {v}') for v in range(1, 21)]
    return months, visitor_types, os_options, browser_options, region_options, traffic_options

MONTH_OPTIONS, VISITOR_OPTIONS, OS_OPTIONS, BROWSER_OPTIONS, REGION_OPTIONS, TRAFFIC_OPTIONS = build_lookup_tables()

INPUT_FIELDS = [
    {'name': 'Administrative', 'label': 'Administrative Pages Visited', 'type': 'number', 'min': 0, 'max': 100, 'step': 1},
    {'name': 'Administrative_Duration', 'label': 'Time Spent on Administrative Pages', 'type': 'number', 'min': 0, 'max': 10000, 'step': 1},
    {'name': 'Informational', 'label': 'Informational Pages Viewed', 'type': 'number', 'min': 0, 'max': 100, 'step': 1},
    {'name': 'Informational_Duration', 'label': 'Time Spent on Informational Pages', 'type': 'number', 'min': 0, 'max': 10000, 'step': 1},
    {'name': 'ProductRelated', 'label': 'Product Pages Viewed', 'type': 'number', 'min': 0, 'max': 1000, 'step': 1},
    {'name': 'ProductRelated_Duration', 'label': 'Time Spent on Product Pages', 'type': 'number', 'min': 0, 'max': 50000, 'step': 1},
    {'name': 'BounceRates', 'label': 'Bounce Rate', 'type': 'number', 'min': 0, 'max': 1, 'step': 0.0001},
    {'name': 'ExitRates', 'label': 'Exit Rate', 'type': 'number', 'min': 0, 'max': 1, 'step': 0.0001},
    {'name': 'PageValues', 'label': 'Page Value Score', 'type': 'number', 'min': 0, 'max': 500, 'step': 0.01},
    {'name': 'SpecialDay', 'label': 'Special Day Proximity', 'type': 'number', 'min': 0, 'max': 1, 'step': 0.01},
]

FEATURE_ORDER = [
    'Administrative',
    'Administrative_Duration',
    'Informational',
    'Informational_Duration',
    'ProductRelated',
    'ProductRelated_Duration',
    'BounceRates',
    'ExitRates',
    'PageValues',
    'SpecialDay',
    'Month',
    'OperatingSystems',
    'Browser',
    'Region',
    'TrafficType',
    'VisitorType',
    'Weekend',
]

CATEGORY_HELPERS = {
    'Month': {v: k for k, v in MONTH_OPTIONS},
    'VisitorType': {
        'Returning Visitor': 'Returning_Visitor',
        'New Visitor': 'New_Visitor',
        'Other': 'Other',
    },
    'Weekend': {'Yes': 1, 'No': 0},
}


def get_dataset_statistics():
    df = pd.read_csv(DATA_PATH)
    total = len(df)
    positive = int((df['Revenue'] == True).sum()) if df['Revenue'].dtype == bool else int((df['Revenue'] == 'True').sum())
    negative = total - positive
    numeric = df.select_dtypes(include=[np.number]).copy()
    numeric['Revenue'] = df['Revenue'].map({False: 0, True: 1, 'False': 0, 'True': 1})
    correlations = numeric.corr()['Revenue'].drop('Revenue').abs().sort_values(ascending=False)
    top_features = [
        {'name': 'Page Values', 'value': round(correlations.get('PageValues', 0), 3)},
        {'name': 'Exit Rates', 'value': round(correlations.get('ExitRates', 0), 3)},
        {'name': 'Product Related Visits', 'value': round(correlations.get('ProductRelated', 0), 3)},
        {'name': 'Bounce Rates', 'value': round(correlations.get('BounceRates', 0), 3)},
        {'name': 'Special Day', 'value': round(correlations.get('SpecialDay', 0), 3)},
    ]
    return {
        'total_sessions': total,
        'purchase_rate': round(positive / total * 100, 1),
        'browse_rate': round(negative / total * 100, 1),
        'positive_sessions': positive,
        'negative_sessions': negative,
        'top_features': top_features,
    }


def build_model_comparison():
    df = pd.read_csv(DATA_PATH)
    df['Revenue'] = df['Revenue'].astype(str)
    X = df.drop('Revenue', axis=1)
    y = target_encoder.transform(df['Revenue'].astype(str))
    for col in ['Month', 'VisitorType']:
        X[col] = label_encoders[col].transform(X[col].astype(str))
    X['Weekend'] = X['Weekend'].astype(str).map({'False': 0, 'True': 1}).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    X_test_scaled = scaler.transform(X_test)
    models = [
        ('MLP', PROJECT_DIR / 'Model' / '01_mlp_model.h5'),
        ('LSTM', PROJECT_DIR / 'Model' / '02_lstm_model.h5'),
        ('GRU', PROJECT_DIR / 'Model' / '03_gru_model.h5'),
        ('Deep Network', PROJECT_DIR / 'Model' / '04_deep_network_model.h5'),
    ]
    items = []
    for name, model_instance in MODEL_REGISTRY.items():
        eval_input = X_test_scaled if name in ['MLP', 'Deep Network'] else X_test_scaled.reshape((X_test_scaled.shape[0], X_test_scaled.shape[1], 1))
        proba = model_instance.predict(eval_input, verbose=0).flatten()
        pred = (proba > 0.5).astype(int)
        items.append({
            'name': name,
            'accuracy': round(float(accuracy_score(y_test, pred)), 4),
            'precision': round(float(precision_score(y_test, pred, zero_division=0)), 4),
            'recall': round(float(recall_score(y_test, pred, zero_division=0)), 4),
            'f1': round(float(f1_score(y_test, pred, zero_division=0)), 4),
            'roc_auc': round(float(roc_auc_score(y_test, proba)), 4),
            'positive_rate': round(float(np.mean(pred) * 100), 2),
            'confusion': None,
        })
    return items


def safe_float(value, minimum, maximum):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return None
    if value < minimum or value > maximum:
        return None
    return value


def generate_prediction_summary(input_values, probability):
    score = round(float(probability * 100), 1)
    model_used = 'Deep Network'
    indicators = []

    if probability >= 0.70:
        title = 'High Purchase Intent Detected'
        description = 'Visitor session behaviour matches high-conversion patterns from historical purchase sessions.'
        if input_values['PageValues'] >= 50:
            indicators.append('Strong page value indicates a high conversion signal.')
        if input_values['ProductRelated'] >= 30:
            indicators.append('High product page interaction suggests active purchase consideration.')
        if input_values['BounceRates'] < 0.10:
            indicators.append('Very low bounce rate signals sustained engagement.')
        if input_values['ExitRates'] < 0.08:
            indicators.append('Low exit rate indicates the visitor remained in the session flow.')
        if input_values['VisitorType'] == 'Returning Visitor':
            indicators.append('Returning visitors often convert at higher rates.')
        if input_values['Weekend'] == 'Yes':
            indicators.append('Weekend traffic shows strong buyer intent in this dataset.')
    elif probability >= 0.40:
        title = 'Moderate Purchase Intent Detected'
        description = 'Visitor behaviour shows some purchase intent, but the session is not yet clearly a strong conversion signal.'
        if input_values['PageValues'] >= 20:
            indicators.append('Moderate page value suggests measurable purchase interest.')
        if input_values['ProductRelated'] >= 15:
            indicators.append('Reasonable product exploration is present in this session.')
        if input_values['BounceRates'] < 0.40:
            indicators.append('Bounce rate is within a moderate range for engaged browsing.')
        if input_values['ExitRates'] < 0.30:
            indicators.append('Exit rate is relatively low, indicating some sustained navigation.')
        if input_values['SpecialDay'] >= 0.5:
            indicators.append('Special day proximity can increase conversion likelihood.')
    else:
        title = 'Low Purchase Intent Detected'
        description = 'This session currently resembles browsing behaviour with weak conversion signals.'
        if input_values['PageValues'] < 20:
            indicators.append('Low page value indicates minimal purchase value signal.')
        if input_values['ProductRelated'] < 15:
            indicators.append('Limited product page interactions point to low purchase interest.')
        if input_values['BounceRates'] > 0.50:
            indicators.append('High bounce rate suggests the visitor left quickly without deep engagement.')
        if input_values['ExitRates'] > 0.30:
            indicators.append('High exit rate indicates the session ended before strong conversion signals emerged.')
        if input_values['SpecialDay'] < 0.5:
            indicators.append('This session is not occurring near a high-conversion special day.')

    if not indicators:
        if probability >= 0.70:
            indicators.append('High session engagement and interaction patterns are driving this prediction.')
        elif probability >= 0.40:
            indicators.append('A mix of browsing and purchase signals are influencing this prediction.')
        else:
            indicators.append('Low engagement metrics and weak purchase indicators are influencing this prediction.')

    return {
        'title': title,
        'description': description,
        'confidence': f'{score}%',
        'probability': f'{probability:.3f}',
        'model': model_used,
        'indicators': indicators,
    }


def preprocess_request(form):
    errors = {}
    values = {}

    for field in INPUT_FIELDS:
        raw = form.get(field['name'])
        value = safe_float(raw, field['min'], field['max'])
        if value is None:
            errors[field['name']] = f'Enter a valid value between {field["min"]} and {field["max"]}.'
        else:
            values[field['name']] = value

    month = form.get('Month')
    if month not in {m[0] for m in MONTH_OPTIONS}:
        errors['Month'] = 'Select a valid month from the dataset options.'
    else:
        values['Month'] = month

    visitor_type = form.get('VisitorType')
    if visitor_type not in {v[0] for v in VISITOR_OPTIONS}:
        errors['VisitorType'] = 'Select a valid visitor type.'
    else:
        values['VisitorType'] = visitor_type

    weekend = form.get('Weekend')
    if weekend not in {'Yes', 'No'}:
        errors['Weekend'] = 'Select whether the session happened over a weekend.'
    else:
        values['Weekend'] = weekend

    for field_name, options in [('OperatingSystems', OS_OPTIONS), ('Browser', BROWSER_OPTIONS), ('Region', REGION_OPTIONS), ('TrafficType', TRAFFIC_OPTIONS)]:
        raw = form.get(field_name)
        if raw not in {opt[0] for opt in options}:
            errors[field_name] = 'Select a valid option from the dataset categories.'
        else:
            values[field_name] = int(raw)

    return values, errors


def encode_input_data(values):
    values['Month'] = label_encoders['Month'].transform([values['Month']])[0]
    values['VisitorType'] = label_encoders['VisitorType'].transform([CATEGORY_HELPERS['VisitorType'][values['VisitorType']]])[0]
    values['Weekend'] = CATEGORY_HELPERS['Weekend'][values['Weekend']]
    ordered = [values[name] for name in FEATURE_ORDER]
    return np.array(ordered, dtype=float).reshape(1, -1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = None
    errors = {}
    form_values = {}
    if request.method == 'POST':
        form_values, errors = preprocess_request(request.form)
        if not errors:
            input_array = encode_input_data(form_values)
            scaled = scaler.transform(input_array)
            probability = float(model.predict(scaled, verbose=0).flatten()[0])
            result = generate_prediction_summary(form_values, probability)
    return render_template(
        'predict.html',
        input_fields=INPUT_FIELDS,
        month_options=MONTH_OPTIONS,
        visitor_options=VISITOR_OPTIONS,
        os_options=OS_OPTIONS,
        browser_options=BROWSER_OPTIONS,
        region_options=REGION_OPTIONS,
        traffic_options=TRAFFIC_OPTIONS,
        result=result,
        errors=errors,
        values=form_values,
    )

@app.route('/dashboard')
def dashboard():
    stats = get_dataset_statistics()
    model_items = build_model_comparison()
    return render_template('dashboard.html', stats=stats, models=model_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
