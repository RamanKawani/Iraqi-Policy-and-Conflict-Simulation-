# routes/conflict_routes.py
from flask import Blueprint

conflict_bp = Blueprint('conflict', __name__)

@conflict_bp.route('/conflict')
def conflict():
    return "Conflict route is working!"
