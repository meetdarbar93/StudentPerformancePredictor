
# 🎓 Student Performance Prediction System

A complete **Machine Learning + Flask Web Application** that predicts:

* 🎯 **Student’s expected score (0–100)**
* 🟢 **Pass/Fail outcome**
* 📊 **Model confidence (%)**

This project includes:

* ✔ Data Cleaning
* ✔ Exploratory Data Analysis
* ✔ Feature Engineering
* ✔ Model Training (Regression + Classification using Random Forest)
* ✔ Model Scaling
* ✔ Flask Web App
* ✔ Notes/Explanation Page
* ✔ Clean Material-UI Styled Frontend
---
# 📁 Project Structure

```
StudentPerformanceProject/

├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── model_utils.py
│   └── templates/
│       ├── index.html
│       ├── result.html
│       └── notes.html
│
├── static/
│   └── css/
│       ├── style.css
│       └── style2.css
│
├── models/
│   ├── best_rf_reg_scaled.pkl
│   ├── best_rf_clf_scaled.pkl
│   └── scaler.pkl
│
├── data/
│   └── cleaned_data.csv
│
├── notebooks/
│   ├── 01_DataCleaning.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_ModelTraining.ipynb
│   └── 04_Tuning.ipynb
│
├── requirements.txt
├── run.py
└── README.md
```

---

# 🚀 Installation Guide

## 1️⃣ Create Virtual Envir		onment

### ● Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### ● Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 2️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
python run.py
```

Now open your browser:

👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

# 💡 How the ML Models Work

This project uses **two models**:

## 1️⃣ Regression Model — Score Prediction

* Predicts student score on a **0–100 scale**
* Uses **RandomForestRegressor + StandardScaler**

## 2️⃣ Classification Model — Pass/Fail

* Predicts **Pass / Fail**
* Also gives **probability (confidence score)**
* Built using **RandomForestClassifier**

Together, these provide accurate, human-like assessments.

---

# 📊 Score Interpretation (Based on Dataset Percentiles)

| Score Range         | Interpretation    |
| ------------------- | ----------------- |
| **75 – 100** | Excellent         |
| **69 – 75**  | Very Good         |
| **62 – 69**  | Good              |
| **38 – 62**  | Needs Improvement |
| **< 38**      | High Risk         |

---

# 🧪 Model Accuracy

## 📘 Regression Model

* **R²:** ~0.75 – 0.82
* **MAE:** 4 – 6
* **RMSE:** 5 – 7

## 📗 Classification Model

* **Accuracy:** ~85% – 92%
* Effective with **attendance**, **previous scores**, and **assignments**.

---

# 🔧 Retraining the Models

Open this notebook:

```
notebooks/03_ModelTraining.ipynb
```

After training, save models:

```
python
joblib.dump(pipe_best_rf, "../models/best_rf_reg_scaled.pkl")
joblib.dump(pipe_best_rf_clf, "../models/best_rf_clf_scaled.pkl")
```

Restart Flask to load new models.

---

# 🙏 Credits

Built by **Meet Darbar**

Technologies Used:

* 🐍 Python
* 🔥 Flask
* 🤖 Scikit-Learn
* 💻 HTML/CSS
* 🎨 Material UI inspired styling

---

# 🎉 DONE!
