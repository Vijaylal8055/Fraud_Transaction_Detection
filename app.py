from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained model (replace this with your actual model)
# For demo, we'll just simulate it
model = RandomForestClassifier()
model.fit([[0, 1, 100]], [0])  # Dummy training
joblib.dump(model, 'model.pkl')  # Save it
model = joblib.load('model.pkl')  # Load it again

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Extract and convert values
    features = [float(data.get(f)) for f in ['feature1', 'feature2', 'amount']]
    prediction = model.predict([features])[0]
    result = "Fraudulent" if prediction == 1 else "Legitimate"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
