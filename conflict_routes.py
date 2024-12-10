from flask import Blueprint, render_template, request, jsonify
from models.conflict_model import ConflictModel

conflict_bp = Blueprint('conflict', __name__)

@conflict_bp.route('/simulate', methods=['POST'])
def simulate_conflict():
    data = request.json
    conflict_model = ConflictModel(
        region=data['region'],
        resources=data['resources'],
        political_factions=data['political_factions']
    )
    result = conflict_model.simulate()
    return jsonify(result)
