import os
from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ensure directories exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)

    with app.app_context():
        # Initialize DB
        from .models import init_db
        init_db()
        
        from . import routes
        app.register_blueprint(routes.bp)

    return app
