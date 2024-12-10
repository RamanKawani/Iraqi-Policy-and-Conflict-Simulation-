from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints (routes)
    from .routes import main
    app.register_blueprint(main)
    
    return app
