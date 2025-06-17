# 🍕 Pizza Restaurant API

A RESTful API built with Flask, SQLAlchemy, and Flask-Migrate to manage pizzas, restaurants, and their menu relationships.

---

## 📁 Project Structure

├── config.py
├── instance
│   └── pizza_api.db
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── 20907511102b_initial_migration.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── server
    ├── app.py
    ├── challenge-1-pizzas.postman_collection.json
    ├── controllers
    │   ├── __init__.py
    │   ├── pizza_controller.py
    │   ├── restaurant_controller.py
    │   └── restaurant_pizza_controller.py
    ├── database.py
    ├── __init__.py
    ├── models
    │   ├── __init__.py
    │   ├── pizza.py
    │   ├── restaurant_pizza.py
    │   └── restaurant.py
    └── seed.py



##  Setup Instructions

### 1. Clone the repo and navigate into it

git clone https://github.com/your-username/pizza_api.git
cd pizza_api

### 2.Create and activate your virtual environment (using Pipenv)
pipenv shell
pipenv install

### 3. Set up the PostgreSQL database and apply migrations
a) Create the PostgreSQL database and user (if not done yet)
Open terminal and run:
sudo -u postgres psql
Inside the psql shell:
CREATE DATABASE pizza_api_db;
CREATE USER pizza_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE pizza_api_db TO pizza_user;
\q
Replace pizza_user and 'your_password' with your actual PostgreSQL username and password.

b) Update your config.py with your database URI
SQLALCHEMY_DATABASE_URI = 'postgresql://pizza_user:your_password@localhost:5432/pizza_api_db'
(Use environment variables if preferred for security.)
c) Run database migrations
flask db upgrade
## 4. Seed the database with initial data
python -m server.seed
## 5. Run the Flask server
flask run
## API Endpoints Overview
Restaurants
GET /restaurants - List all restaurants

GET /restaurants/<id> - Get a single restaurant with its pizzas

DELETE /restaurants/<id> - Delete a restaurant and its associated restaurant_pizzas

Pizzas
GET /pizzas - List all pizzas

RestaurantPizzas
POST /restaurant_pizzas - Add a pizza to a restaurant’s menu
Body example:

json
Copy code
{
  "restaurant_id": 1,
  "pizza_id": 2,
  "price": 12
}
 Testing
Use the included Postman collection challenge-1-pizzas.postman_collection.json in the server/ folder to test the API endpoints.

## Tech Stack
Python 3.x

Flask

Flask-Migrate (Alembic)

SQLAlchemy ORM

PostgreSQL

Pipenv for dependency management

