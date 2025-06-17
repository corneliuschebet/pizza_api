from server.database import db
from sqlalchemy.orm import validates

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

    # One-to-many: Restaurant → RestaurantPizzas
    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete-orphan'
    )

    def to_dict(self, include_pizzas=False):
        data = {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
        if include_pizzas:
            data['pizzas'] = [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        return data

    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip()

    @validates('address')
    def validate_address(self, key, value):
        if not value or not value.strip():
            raise ValueError("Address cannot be empty")
        return value.strip()

    def __repr__(self):
        return f"<Restaurant {self.name}>"
