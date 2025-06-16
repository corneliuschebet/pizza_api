from flask import Flask
from flask_migrate import Migrate
from config import Config
from database import db

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Import models after db initialization
from models import Restaurant, Pizza, RestaurantPizza

# Import and register blueprints
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def index():
    return {'message': 'Pizza Restaurant API is running!'}, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)