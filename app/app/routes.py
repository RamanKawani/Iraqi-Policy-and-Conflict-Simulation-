from flask import Blueprint, render_template, request
from app.simulation import run_simulation

# Blueprint to handle routes related to the main part of the app
main = Blueprint('main', __name__)

# Route for the homepage
@main.route('/')
def index():
    return render_template('index.html')  # Render input page for policy and scenario

# Route for simulating policy outcomes
@main.route('/simulate', methods=['POST'])
def simulate():
    policy_id = request.form['policy_id']
    scenario = request.form['scenario']
    
    # Call the simulation function and pass the policy_id and scenario
    simulation_result = run_simulation(policy_id, scenario)
    
    # Display the result on the result page
    return render_template('simulation_result.html', result=simulation_result)
