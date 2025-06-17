from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.database import db

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    """GET /restaurants - Retrieve all restaurants"""
    try:
        restaurants = Restaurant.query.all()
        return jsonify([r.to_dict() for r in restaurants]), 200
    except Exception as e:
        return jsonify({'error': 'Failed to fetch restaurants', 'message': str(e)}), 500

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    """GET /restaurants/<id> - Retrieve a specific restaurant with its pizzas"""
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.to_dict(include_pizzas=True)), 200

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    """DELETE /restaurants/<id> - Delete a restaurant and its associations"""
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    try:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete restaurant', 'message': str(e)}), 500
