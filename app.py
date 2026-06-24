from flask import Flask, render_template, request, jsonify
from pathlib import Path
import pickle
import pandas as pd
import os
from recommendations import get_recommendations

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"

app = Flask(__name__, template_folder=str(BASE_DIR / "templates"))


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Missing model file: {MODEL_PATH}. Run train_model.py first to generate it."
        )

    with MODEL_PATH.open('rb') as f:
        return pickle.load(f)


# Load model
model, label_encoders = load_model()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        age = float(data['age'])
        gender = data['gender']
        bmi = float(data['bmi'])
        bp = float(data['bp'])
        sugar = float(data['sugar'])
        cholesterol = float(data['cholesterol'])
        smoking = data['smoking']
        family_history = data['familyHistory']

        gender_enc = label_encoders['Gender'].transform([gender])[0]
        smoking_enc = label_encoders['Smoking'].transform([smoking])[0]
        family_enc = label_encoders['FamilyHistory'].transform([family_history])[0]

        features = pd.DataFrame(
            [[age, gender_enc, bmi, bp, sugar, cholesterol, smoking_enc, family_enc]],
            columns=["Age", "Gender", "BMI", "BP", "Sugar", "Cholesterol", "Smoking", "FamilyHistory"]
        )

        prediction_idx = model.predict(features)[0]
        prediction = label_encoders['Disease'].inverse_transform([prediction_idx])[0]

        probabilities = model.predict_proba(features)[0]
        classes = label_encoders['Disease'].classes_
        prob_dict = {cls: round(float(prob) * 100, 1) for cls, prob in zip(classes, probabilities)}

        # Get the rule-based recommendation bundle for this prediction
        recommendations = get_recommendations(prediction)

        return jsonify({
            'success': True,
            'prediction': prediction,
            'probabilities': prob_dict,
            'recommendations': recommendations
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=False, use_reloader=False)
