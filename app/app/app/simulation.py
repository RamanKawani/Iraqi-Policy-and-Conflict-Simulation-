import random

def run_simulation(policy_id, scenario):
    # This function simulates the outcome of a policy under a scenario
    
    # Example of a simple outcome based on random selection
    possible_outcomes = ['Positive Impact', 'Neutral Impact', 'Negative Impact']
    
    # Simulate the outcome (this could be replaced with more sophisticated logic later)
    outcome = random.choice(possible_outcomes)
    
    # Prepare the simulation result
    simulation_result = {
        'policy_id': policy_id,
        'scenario': scenario,
        'outcome': outcome,
        'details': f'The simulation for policy {policy_id} under scenario {scenario} resulted in: {outcome}'
    }
    
    return simulation_result
