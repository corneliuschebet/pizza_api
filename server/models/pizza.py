from database import db
from sqlalchemy.orm import validates

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    
    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', 
                                      backref='pizza')
    
    def to_dict(self):
        """Convert Pizza instance to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }
    
    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        return name.strip()
    
    @validates('ingredients')
    def validate_ingredients(self, key, ingredients):
        if not ingredients or len(ingredients.strip()) == 0:
            raise ValueError("Ingredients cannot be empty")
        return ingredients.strip()
    
    def __repr__(self):
        return f'<Pizza {self.name}>'