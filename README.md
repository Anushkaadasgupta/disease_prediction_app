# 🩺 Disease Prediction Web App

A simple **Flask-based web application** that predicts disease risk based on user inputs like age, gender, smoking habits, family history, and BMI using a trained Machine Learning model.

---

## 🚀 Features

* User-friendly web interface
* Takes health-related inputs
* Encodes categorical data
* Uses a trained ML model (`model.pkl`)
* Displays prediction results instantly

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS
* **Backend**: Python (Flask)
* **Libraries**: NumPy, Pickle
* **Model**: Machine Learning (trained externally)

---

## 📁 Project Structure

```
disease_prediction_app/
│
├── app.py
├── model.pkl
├── health_data.csv
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/disease_prediction_app.git
cd disease_prediction_app
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate it:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install flask numpy
```

---

## ▶️ Run the App

```
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📊 How It Works

1. User enters details in form
2. Data is sent to backend (`/predict`)
3. Categorical values are encoded
4. Model predicts result
5. Output is displayed on result page

---

## ⚠️ Important Notes

* `model.pkl` must be present in the root folder
* Ensure correct folder structure (`templates/`)
* Do not upload `venv/` or unnecessary files

---

## 🌟 Future Improvements

* Add more diseases
* Improve UI design
* Deploy online (Render / Railway / AWS)
* Add user authentication

---

## 👨‍💻 Author

**Your Name**
GitHub: https://github.com/your-username

---

## 📜 License

This project is for educational purposes.
