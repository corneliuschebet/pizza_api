from flask import Blueprint, request, jsonify
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.database import db

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    """
    POST /restaurant_pizzas - Create a new RestaurantPizza association
    Body: { price, pizza_id, restaurant_id }
    """
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate input
    errors = []

    if price is None or not isinstance(price, int) or price < 1 or price > 30:
        errors.append("Price must be between 1 and 30")

    if not pizza_id:
        errors.append("Pizza ID is required")

    if not restaurant_id:
        errors.append("Restaurant ID is required")

    # Check if related records exist
    pizza = Pizza.query.get(pizza_id) if pizza_id else None
    restaurant = Restaurant.query.get(restaurant_id) if restaurant_id else None

    if pizza_id and not pizza:
        errors.append("Pizza not found")
    if restaurant_id and not restaurant:
        errors.append("Restaurant not found")

    if errors:
        return jsonify({"errors": errors}), 400

    # Create and commit the RestaurantPizza
    try:
        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()
        return jsonify(rp.to_dict(include_relations=True)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create RestaurantPizza", "message": str(e)}), 500
