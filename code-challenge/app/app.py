#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import Hero, Power, HeroPower

from models import db, Hero

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Welcome to the Heros page for all anime lovers</h1>'


# Helper function to create JSON responses
def create_json_response(data, status_code=200):
    response = make_response(jsonify(data), status_code)
    response.headers['Content-Type'] = 'application/json'
    return response

# Route to get a list of all heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [
        {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }
        for hero in heroes
    ]
    return create_json_response(heroes_data)

# Route to get details of a specific hero by ID
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return create_json_response({"error": "Hero not found"}, 404)

    #  Else we Retrieve the hero's powers
    powers = [
        {
            "id": hero_power.power.id,
            "name": hero_power.power.name,
            "description": hero_power.power.description
        }
        for hero_power in hero.powers
    ]

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": powers
    }
    return create_json_response(hero_data)

# Route to get a list of all powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [
        {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        for power in powers
    ]
    return create_json_response(powers_data)

# Route to get details of a specific power by ID
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power is None:
        return create_json_response({"error": "Power not found"}, 404)

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    return create_json_response(power_data)

# Route to update an existing power by ID
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    # Get the power by ID
    power = Power.query.get(id)
    if power is None:
        return create_json_response({"error": "Power not found"}, 404)

    # Get the updated description from the request body
    data = request.get_json()
    if 'description' not in data:
        return create_json_response({"errors": ["description is required"]}, 400)

    updated_description = data['description']
    if len(updated_description) < 20:
        return create_json_response({"errors": ["Description must be at least 20 characters long."]}, 400)

    # Update the power's description and commit changes to the database
    power.description = updated_description
    db.session.commit()

    # Return the updated power data
    updated_power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    return create_json_response(updated_power_data)


# Route to create a new HeroPower
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    # Get data from the request body
    data = request.get_json()

    # Validate and extract the required properties
    required_properties = ['strength', 'power_id', 'hero_id']
    for prop in required_properties:
        if prop not in data:
            return create_json_response({"errors": [f"{prop} is required"]}, 400)

    # Validate the 'strength' property
    allowed_strengths = ['Strong', 'Weak', 'Average']
    if data['strength'] not in allowed_strengths:
        return create_json_response({"errors": ["Invalid strength. Allowed values are 'Strong', 'Weak', 'Average'."]}, 400)

    # Get the associated Hero and Power
    hero = Hero.query.get(data['hero_id'])
    power = Power.query.get(data['power_id'])

    if hero is None or power is None:
        return create_json_response({"errors": ["Hero or Power not found"]}, 404)

    # Create and add the new HeroPower to the database
    hero_power = HeroPower(
        hero=hero,
        power=power,
        strength=data['strength']
    )
    db.session.add(hero_power)
    db.session.commit()

    # Retrieve the hero's powers
    powers = [
        {
            "id": hero_power.power.id,
            "name": hero_power.power.name,
            "description": hero_power.power.description
        }
        for hero_power in hero.powers
    ]

    # Return the hero's data with associated powers
    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": powers
    }
    return create_json_response(hero_data)


if __name__ == '__main__':
    app.run(port=5555)
