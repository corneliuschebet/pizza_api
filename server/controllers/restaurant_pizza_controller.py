from flask import Blueprint, jsonify, request
from database import db
from models.restaurant_pizza import RestaurantPizza
from models.restaurant import Restaurant
from models.pizza import Pizza
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    """Create a new RestaurantPizza association"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'errors': ['No data provided']}), 400
        
        # Extract required fields
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')
        
        # Validate required fields
        errors = []
        if price is None:
            errors.append('Price is required')
        if pizza_id is None:
            errors.append('Pizza ID is required')
        if restaurant_id is None:
            errors.append('Restaurant ID is required')
        
        if errors:
            return jsonify({'errors': errors}), 400
        
        # Check if restaurant exists
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'errors': ['Restaurant not found']}), 400
        
        # Check if pizza exists
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return jsonify({'errors': ['Pizza not found']}), 400
        
        # Create new RestaurantPizza
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify(restaurant_pizza.to_dict(include_relations=True)), 201
        
    except ValueError as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'errors': ['Database integrity error']}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 500