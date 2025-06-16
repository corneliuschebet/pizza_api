from database import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    def to_dict(self, include_relations=False):
        """Convert RestaurantPizza instance to dictionary"""
        result = {
            'id': self.id,
            'price': self.price,
            'pizza_id': self.pizza_id,
            'restaurant_id': self.restaurant_id
        }
        
        if include_relations:
            result['pizza'] = self.pizza.to_dict()
            result['restaurant'] = self.restaurant.to_dict()
        
        return result
    
    @validates('price')
    def validate_price(self, key, price):
        if price is None:
            raise ValueError("Price is required")
        if not isinstance(price, int) or price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30")
        return price
    
    @validates('restaurant_id')
    def validate_restaurant_id(self, key, restaurant_id):
        if restaurant_id is None:
            raise ValueError("Restaurant ID is required")
        return restaurant_id
    
    @validates('pizza_id')
    def validate_pizza_id(self, key, pizza_id):
        if pizza_id is None:
            raise ValueError("Pizza ID is required")
        return pizza_id
    
    def __repr__(self):
        return f'<RestaurantPizza {self.restaurant_id}-{self.pizza_id}>'