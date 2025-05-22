from flask import Flask, request, render_template
import joblib
from feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load('phishing_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    result = model.predict([features])[0]
    output = "⚠️ Phishing Website" if result == 1 else "✅ Safe Website"
    return render_template('index.html', result=output)

if __name__ == '__main__':
    app.run(debug=True)
