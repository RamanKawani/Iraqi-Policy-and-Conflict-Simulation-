# routes/policy_routes.py
from flask import Blueprint

policy_bp = Blueprint('policy', __name__)

@policy_bp.route('/policy')
def policy():
    return "Policy route is working!"
