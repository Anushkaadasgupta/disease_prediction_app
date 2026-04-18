from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model, label_encoders = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form inputs
        age = int(request.form['age'])
        gender = request.form['gender']
        smoking = request.form['smoking']
        family_history = request.form['family_history']
        bmi = float(request.form['bmi'])

        # Encode categorical values using saved encoders
        gender_encoded = label_encoders['Gender'].transform([gender])[0]
        smoking_encoded = label_encoders['Smoking'].transform([smoking])[0]
        family_encoded = label_encoders['FamilyHistory'].transform([family_history])[0]

        # Create input array
        input_data = np.array([[age, gender_encoded, smoking_encoded, family_encoded, bmi]])

        # Predict using the model
        prediction_encoded = model.predict(input_data)[0]

        # Decode predicted label
        prediction = label_encoders['Disease'].inverse_transform([prediction_encoded])[0]

        return render_template('result.html', prediction=prediction)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
