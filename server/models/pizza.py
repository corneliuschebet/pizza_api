from server.database import db
from sqlalchemy.orm import validates

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)

    # One-to-many: Pizza → RestaurantPizzas
    restaurant_pizzas = db.relationship(
        'RestaurantPizza',
        back_populates='pizza',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        return value.strip()

    @validates('ingredients')
    def validate_ingredients(self, key, value):
        if not value or not value.strip():
            raise ValueError("Ingredients cannot be empty")
        return value.strip()

    def __repr__(self):
        return f"<Pizza {self.name}>"
