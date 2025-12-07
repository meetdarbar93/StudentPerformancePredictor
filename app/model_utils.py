import numpy as np
import pandas as pd
import joblib

def load_pickle(path):
    return joblib.load(path)

def prepare_features(form_data, scaler=None):
    part_map = {'Low': 0, 'Medium': 1, 'High': 2}
    part = part_map.get(form_data.get('participation', 'Medium'), 1)

    data = {
        'Hours_Studied': [float(form_data.get('hours_studied', 0))],
        'Attendance': [float(form_data.get('attendance', 0))],
        'Previous_Score': [float(form_data.get('previous_score', 0))],
        'Assignments_Completed': [float(form_data.get('assignments_completed', 0))],
        'Sleep_Hours': [float(form_data.get('sleep_hours', 0))],
        'Participation': [part]
    }

    return pd.DataFrame(data)

def predict_both(model_reg, model_clf, X):
    score_pred = model_reg.predict(X)[0]

    prob = None
    if hasattr(model_clf, "predict_proba"):
        prob = model_clf.predict_proba(X)[0][1]   # prob of PASS

    # ----- Decide Pass/Fail -----
    if score_pred >= 40:
        pass_pred = 1
    else:
        if prob is not None and prob >= 0.50:
            pass_pred = 1
        else:
            pass_pred = 0

    # ----- Confidence -----
    if prob is None:
        confidence = None
    else:
        # base confidence from classifier
        conf_prob = prob

        # extra boost from high score (scale score 0–100 → 0–1)
        conf_score = score_pred / 100.0

        # combine (you can adjust 0.5 & 0.5)
        confidence = 0.5 * conf_prob + 0.5 * conf_score
        confidence = max(0.0, min(1.0, confidence))

    return {
        'pred_score': score_pred,
        'pred_pass': 'Pass' if pass_pred == 1 else 'Fail',
        'confidence': confidence
    }
