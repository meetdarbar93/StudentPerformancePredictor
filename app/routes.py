from flask import Blueprint, render_template, request, flash, current_app
import os
from app.model_utils import load_pickle, prepare_features, predict_both

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@routes_bp.route('/notes')
def notes():
    return render_template('notes.html')


@routes_bp.route('/predict', methods=['GET', 'POST'])
def make_prediction():

    # GET request → show form
    if request.method == 'GET':
        return render_template('index.html')

    # POST request → handle prediction
    try:
        data = request.form

        # Load correct model paths
        reg_model_path = current_app.config.get('MODEL_PATH')
        clf_model_path = current_app.config.get('CLASSIFIER_PATH')

        # Check model files exist
        if not os.path.exists(reg_model_path):
            flash("Regression model not found", "danger")
            return render_template('index.html')

        if not os.path.exists(clf_model_path):
            flash("Classifier model not found", "danger")
            return render_template('index.html')

        reg_model = load_pickle(reg_model_path)
        clf_model = load_pickle(clf_model_path)

        features = prepare_features(data)

        result = predict_both(reg_model, clf_model, features)

        return render_template("result.html", result=result, inputs=data)

    except Exception as e:
        # SHOW THE REAL ERROR IN TERMINAL
        print("\n🔥 BACKEND ERROR:", e, "\n")
        flash("Something went wrong while making prediction.", "danger")
        return render_template('index.html')
