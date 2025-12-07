from flask import Flask

def create_app():

    app = Flask(__name__)
    app.secret_key = "student"

    app.config['MODEL_PATH'] = 'models/best_rf_reg_scaled.pkl'
    app.config['CLASSIFIER_PATH'] = 'models/best_rf_clf_scaled.pkl'

    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
