from database import db
from sqlalchemy.orm import validates

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', 
                                      backref='restaurant', 
                                      cascade='all, delete-orphan')
    
    def to_dict(self, include_pizzas=False):
        """Convert Restaurant instance to dictionary"""
        result = {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }
        
        if include_pizzas:
            result['pizzas'] = [
                rp.pizza.to_dict() for rp in self.restaurant_pizzas
            ]
        
        return result
    
    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        return name.strip()
    
    @validates('address')
    def validate_address(self, key, address):
        if not address or len(address.strip()) == 0:
            raise ValueError("Address cannot be empty")
        return address.strip()
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'