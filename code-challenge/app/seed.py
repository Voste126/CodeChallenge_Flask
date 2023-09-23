#!/usr/bin/env python3

from random import choice as rc
import random
from faker import Faker

from app import app
from models import Hero, Power, HeroPower ,db

fake = Faker()

def seed_data():

    # Clear existing data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Seeding powers
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    powers = []
    for power_info in powers_data:
        power = Power(**power_info)
        powers.append(power)

    db.session.add_all(powers)

    # Seeding heroes
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    heroes = []
    for hero_info in heroes_data:
        hero = Hero(**hero_info)
        heroes.append(hero)

    db.session.add_all(heroes)

    # Adding powers to heroes
    strengths = ["Strong", "Weak", "Average"]
    for hero in heroes:
        for _ in range(random.randint(1, 3)):  # Randomly assign 1 to 3 powers to each hero
            power = rc(powers)
            hero_power = HeroPower(hero=hero, power=power, strength=rc(strengths))
            db.session.add(hero_power)

    # Commit changes to the database
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
