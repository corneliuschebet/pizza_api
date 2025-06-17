from server.database import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    # Many-to-one relationships
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    def to_dict(self, include_relations=False):
        data = {
            'id': self.id,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'pizza_id': self.pizza_id
        }
        if include_relations:
            data['restaurant'] = self.restaurant.to_dict()
            data['pizza'] = self.pizza.to_dict()
        return data

    @validates('price')
    def validate_price(self, key, value):
        if not isinstance(value, int) or not (1 <= value <= 30):
            raise ValueError("Price must be between 1 and 30")
        return value

    @validates('restaurant_id', 'pizza_id')
    def validate_foreign_keys(self, key, value):
        if value is None:
            raise ValueError(f"{key.replace('_', ' ').capitalize()} is required")
        return value

    def __repr__(self):
        return f"<RestaurantPizza R{self.restaurant_id}-P{self.pizza_id}>"
