import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'model.pkl'

# Extended dataset (your original 15 rows + more synthetic data for better model)
data = {
    'Age': [45,56,38,28,63,35,50,47,60,33,54,41,29,65,36,
            52,44,31,67,39,55,42,27,61,48,34,58,43,26,70,
            49,37,62,46,30,53,40,25,64,51],
    'Gender': ['Male','Female','Male','Female','Male','Female','Male','Male','Female','Male',
               'Female','Male','Female','Male','Female',
               'Male','Female','Male','Female','Male','Female','Male','Female','Male','Female',
               'Male','Female','Male','Female','Male',
               'Female','Male','Male','Female','Female','Male','Female','Male','Female','Male'],
    'BMI': [28.5,32.1,25.3,22.0,29.4,31.5,27.0,26.2,33.5,23.8,
            30.0,26.4,24.1,34.2,29.9,
            27.5,31.0,24.5,35.0,25.8,30.5,27.8,22.5,32.0,28.0,
            24.0,29.0,26.0,21.5,36.0,
            28.8,25.5,31.2,27.2,23.0,29.5,26.8,22.8,33.0,28.2],
    'BP': [130,120,140,110,150,135,138,128,145,115,
           132,137,118,148,125,
           134,122,112,152,118,136,130,108,147,129,
           116,142,127,109,155,
           131,119,143,128,111,139,126,107,149,133],
    'Sugar': [180,90,160,80,200,85,170,150,95,89,
              140,155,99,210,145,
              165,88,82,205,92,175,158,78,208,148,
              86,168,152,76,215,
              162,84,172,154,81,178,146,79,202,167],
    'Cholesterol': [220,180,210,170,240,190,230,200,185,178,
                    215,225,182,250,210,
                    218,182,172,245,180,228,205,168,248,202,
                    174,222,198,165,255,
                    212,176,235,208,173,232,194,167,244,218],
    'Smoking': ['Yes','No','No','No','Yes','No','Yes','Yes','No','No',
                'Yes','No','No','Yes','No',
                'Yes','No','No','Yes','No','Yes','No','No','Yes','No',
                'No','Yes','No','No','Yes',
                'No','No','Yes','No','No','Yes','No','No','Yes','Yes'],
    'FamilyHistory': ['Yes','No','Yes','No','Yes','No','Yes','Yes','No','No',
                      'Yes','No','No','Yes','Yes',
                      'Yes','No','No','Yes','No','Yes','Yes','No','Yes','No',
                      'No','Yes','No','No','Yes',
                      'No','No','Yes','No','No','Yes','No','No','Yes','Yes'],
    'Disease': ['Diabetes','No Disease','Diabetes','No Disease','Heart Disease','No Disease',
                'Heart Disease','Diabetes','No Disease','No Disease','Heart Disease','Diabetes',
                'No Disease','Heart Disease','Diabetes',
                'Heart Disease','No Disease','No Disease','Heart Disease','No Disease',
                'Heart Disease','Diabetes','No Disease','Heart Disease','Diabetes',
                'No Disease','Heart Disease','Diabetes','No Disease','Heart Disease',
                'No Disease','No Disease','Heart Disease','Diabetes','No Disease',
                'Heart Disease','No Disease','No Disease','Heart Disease','Diabetes']
}

df = pd.DataFrame(data)

# Encode categorical features
le_gender = LabelEncoder()
le_smoking = LabelEncoder()
le_family = LabelEncoder()
le_disease = LabelEncoder()

df['Gender'] = le_gender.fit_transform(df['Gender'])
df['Smoking'] = le_smoking.fit_transform(df['Smoking'])
df['FamilyHistory'] = le_family.fit_transform(df['FamilyHistory'])
df['Disease'] = le_disease.fit_transform(df['Disease'])

X = df.drop('Disease', axis=1)
y = df['Disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc * 100:.1f}%")
print(f"Classes: {le_disease.classes_}")

label_encoders = {
    'Gender': le_gender,
    'Smoking': le_smoking,
    'FamilyHistory': le_family,
    'Disease': le_disease
}

with MODEL_PATH.open('wb') as f:
    pickle.dump((model, label_encoders), f)

print(f"Model saved to {MODEL_PATH}")
