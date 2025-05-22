from flask import Flask, request, render_template
import joblib
from feature_extractor import extract_features_from_form  # Correct import

app = Flask(__name__)
model = joblib.load('phishing_model.pkl')  # Load once at startup

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form
    features = extract_features_from_form(form_data)
    result = model.predict([features])[0]
    return "Phishing Website" if result == 1 else "Safe Website"

if __name__ == '__main__':
    app.run(debug=True)
