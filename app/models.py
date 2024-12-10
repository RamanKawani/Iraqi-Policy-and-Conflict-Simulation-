from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Policy Model to store different policies
class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    scenarios = db.relationship('Scenario', backref='policy', lazy=True)

# Scenario Model to store scenarios for each policy
class Scenario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'), nullable=False)
    outcome = db.Column(db.String(255))  # Result of the scenario

# Simulation Result Model to store simulation results
class SimulationResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'))
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.id'))
    outcome = db.Column(db.String(100))
    details = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
