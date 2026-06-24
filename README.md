# CardioGluco

A Flask-based ML web app that predicts risk of **Diabetes**, **Heart Disease**, or **No Disease** based on patient health parameters.

## Features
- Random Forest classifier
- Responsive UI with animated sliders
- Probability breakdown for all 3 classes
- Production-ready with Gunicorn

## Local Run
```bash
pip install -r requirements.txt
python train_model.py
python app.py
```

Visit http://localhost:5000

## Deploy to Render

1. Push this project to a GitHub repository.
2. Go to [render.com](https://render.com) and create a new **Web Service** or **Blueprint**.
3. Connect your GitHub repo.
4. Use these values if you are setting it manually:
   - Build Command: `pip install -r requirements.txt && python train_model.py`
   - Start Command: `gunicorn app:app`
   - Environment: Python 3.11
5. Deploy the service.

The included [render.yaml](/render.yaml) file can auto-configure the service on Render.

## Input Parameters
| Field | Description |
|---|---|
| Age | Patient age (18-90) |
| Gender | Male / Female |
| BMI | Body Mass Index |
| BP | Blood Pressure (mmHg) |
| Sugar | Blood Sugar (mg/dL) |
| Cholesterol | Cholesterol level (mg/dL) |
| Smoking | Yes / No |
| Family History | Yes / No |

## Disclaimer
For educational and portfolio purposes only. Not a substitute for medical advice.
