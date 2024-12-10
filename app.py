# app.py
from flask import Flask
from routes.policy_routes import policy_bp
from routes.conflict_routes import conflict_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(policy_bp)
app.register_blueprint(conflict_bp)

@app.route('/')
def home():
    return "Welcome to the Iraqi Policy and Conflict Simulation!"

if __name__ == '__main__':
    app.run(debug=True)

