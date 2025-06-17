from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    """Seed the database with initial data"""
    
    app = create_app()

    with app.app_context():
    
        print("Clearing existing data...")
        RestaurantPizza.query.delete()
        Restaurant.query.delete()
        Pizza.query.delete()
        
        
        print("Creating restaurants...")
        restaurants = [
            Restaurant(
                name="Sottocasa NYC",
                address="298 Atlantic Ave, Brooklyn, NY 11201"
            ),
            Restaurant(
                name="PizzArte",
                address="69 W 55th St, New York, NY 10019"
            ),
            Restaurant(
                name="Kiki's Pizza",
                address="227 Front St, New York, NY 10038"
            )
        ]
        
        for restaurant in restaurants:
            db.session.add(restaurant)
        
        
        print("Creating pizzas...")
        pizzas = [
            Pizza(
                name="Cheese",
                ingredients="Dough, Tomato Sauce, Cheese"
            ),
            Pizza(
                name="Pepperoni",
                ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"
            ),
            Pizza(
                name="California",
                ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard"
            ),
            Pizza(
                name="Margherita",
                ingredients="Dough, Tomato Sauce, Fresh Mozzarella, Basil"
            ),
            Pizza(
                name="Hawaiian",
                ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple"
            )
        ]
        
        for pizza in pizzas:
            db.session.add(pizza)
        
        
        db.session.commit()
        
        
        print("Creating restaurant-pizza associations...")
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=4),
            RestaurantPizza(price=8, restaurant_id=2, pizza_id=1),
            RestaurantPizza(price=11, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=13, restaurant_id=2, pizza_id=5),
            RestaurantPizza(price=9, restaurant_id=3, pizza_id=2),
            RestaurantPizza(price=14, restaurant_id=3, pizza_id=4),
            RestaurantPizza(price=16, restaurant_id=3, pizza_id=5)
        ]
        
        for rp in restaurant_pizzas:
            db.session.add(rp)
        
        db.session.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(restaurants)} restaurants")
        print(f"Created {len(pizzas)} pizzas")
        print(f"Created {len(restaurant_pizzas)} restaurant-pizza associations")

if __name__ == '__main__':
    seed_data()
