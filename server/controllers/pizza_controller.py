from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    """GET /pizzas - Retrieve all pizzas"""
    try:
        pizzas = Pizza.query.all()
        return jsonify([pizza.to_dict() for pizza in pizzas]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve pizzas', 'message': str(e)}), 500
