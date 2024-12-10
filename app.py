from flask import Flask, render_template, request, jsonify
from routes.policy_routes import policy_bp
from routes.conflict_routes import conflict_bp
from config import Config

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Register the blueprints for the different parts of the app
app.register_blueprint(policy_bp, url_prefix='/policy')
app.register_blueprint(conflict_bp, url_prefix='/conflict')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
