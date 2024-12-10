# app/__init__.py

def create_app():
    from flask import Flask  # Import Flask inside the function to avoid circular imports
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the database
    from .models import db
    db.init_app(app)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
