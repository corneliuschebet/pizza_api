from flask import Blueprint, jsonify, request
from database import db
from models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    """Get all restaurants"""
    try:
        restaurants = Restaurant.query.all()
        return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    """Get a single restaurant with its pizzas"""
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
        
        return jsonify(restaurant.to_dict(include_pizzas=True)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    """Delete a restaurant and all related RestaurantPizzas"""
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
        
        # The cascade='all, delete-orphan' in the model will handle
        # deleting related RestaurantPizzas automatically
        db.session.delete(restaurant)
        db.session.commit()
        
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500