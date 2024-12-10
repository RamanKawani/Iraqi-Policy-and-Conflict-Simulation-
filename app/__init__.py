from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load config from config.py
    
    # Register routes (from routes.py)
    from .routes import main
    app.register_blueprint(main)

    return app
