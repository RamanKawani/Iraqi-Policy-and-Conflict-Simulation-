from flask import Blueprint, render_template, request
from app.simulation import run_simulation
from app.data_processing import get_policy_data
from app.models import db, Policy, Scenario, SimulationResult

main = Blueprint('main', __name__)

# Route to display all policies
@main.route('/')
def index():
    policies = Policy.query.all()  # Fetch all policies from the database
    return render_template('index.html', policies=policies)

# Route to display details of a policy
@main.route('/policy/<int:policy_id>')
def policy_detail(policy_id):
    policy = Policy.query.get_or_404(policy_id)  # Fetch policy details
    return render_template('policy_detail.html', policy=policy)

# Route for simulating policy outcomes
@main.route('/simulate', methods=['POST'])
def simulate():
    policy_id = request.form['policy_id']
    scenario_id = request.form['scenario_id']
    
    # Fetch policy and scenario data from the database
    policy = Policy.query.get(policy_id)
    scenario = Scenario.query.get(scenario_id)
    
    # Run the simulation
    simulation_result = run_simulation(policy, scenario)
    
    # Store simulation result in the database
    result = SimulationResult(policy_id=policy.id, scenario_id=scenario.id, 
                              outcome=simulation_result['outcome'], 
                              details=simulation_result['details'])
    db.session.add(result)
    db.session.commit()
    
    return render_template('simulation_result.html', result=simulation_result)
