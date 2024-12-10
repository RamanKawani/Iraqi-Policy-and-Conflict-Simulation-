from flask import Blueprint, render_template, request, jsonify
from models.policy_model import PolicyModel

policy_bp = Blueprint('policy', __name__)

@policy_bp.route('/simulate', methods=['POST'])
def simulate_policy():
    data = request.json
    policy_model = PolicyModel(
        government_type=data['government_type'],
        economic_state=data['economic_state'],
        foreign_relations=data['foreign_relations']
    )
    result = policy_model.simulate_policy_outcome()
    return jsonify(result)
