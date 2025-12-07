
---
# 🎓 Student Performance Prediction System

A complete **Machine Learning + Flask Web App** that predicts:

- **Student’s expected score (0–100)**
- **Pass/Fail outcome**
- **Confidence level (%)**

This project includes:

✔ Data Cleaning  
✔ Exploratory Data Analysis  
✔ Feature Engineering  
✔ Model Training (Random Forest Regression + Classification)  
✔ Scaling  
✔ Flask Web App  
✔ Notes/Explanation Page  
✔ Beautiful Material-UI Style Frontend  

---

#📁 Project Structure



StudentPerformanceProject/

│

├── app/

│   ├── **init**.py

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

│    ├── 01_DataCleaning.ipynb

│   ├── 02_EDA.ipynb

│   ├── 03_ModelTraining.ipynb

│   └── 04_Tuning.ipynb

│

├── requirements.txt

├── run.py

└── README.md


---

# 🚀 Installation

### 1. Create Virtual Environment

Windows:
```
python -m venv venv
venv\Scripts\activate

```

Mac/Linux:
```

python3 -m venv venv
source venv/bin/activate

```

### 2. Install Dependencies
```

pip install -r requirements.txt

```

---

## ▶️ Run the App

```

python run.py

```

Open browser:  
👉 http://127.0.0.1:5000/

---

## 💡 How The Model Works

Two ML models are used:

### 1️⃣ Regression Model (Score Prediction)
Predicts score on **0–100 scale**  
Trained using RandomForestRegressor with StandardScaler.

### 2️⃣ Classification Model (Pass/Fail)
Predicts pass/fail + confidence probability  
Trained using RandomForestClassifier.

This gives natural and human-like predictions.

---

## 📊 Score Meaning (Based on Dataset Percentiles)

| Range | Meaning |
|-------|---------|
| **75 – 100** | Excellent |
| **69 – 75**  | Very Good |
| **62 – 69**  | Good |
| **38 – 62**  | Needs Improvement |
| **< 38**     | High Risk |

---

## 🧪 Model Accuracy

### Regression:
- R² ≈ **0.75 – 0.82**
- MAE ≈ **4 – 6**
- RMSE ≈ **5 – 7**

### Classification:
- Accuracy ≈ **85% – 92%**
- Strong performance on attendance + previous scores

---

## 🛠 Retraining the Model

Open:
```

03_ModelTraining.ipynb

```

Run all cells, then save:

```

joblib.dump(pipe_best_rf, "../models/best_rf_reg_scaled.pkl")
joblib.dump(pipe_best_rf_clf, "../models/best_rf_clf_scaled.pkl")

```

Restart Flask.


---

## 🙏 Credits

Made by **Meet Darbar**  
Built using:
- Python  
- Flask  
- Scikit-Learn  
- HTML/CSS  
- Material Design UI  

---


# 🎉 DONE!

