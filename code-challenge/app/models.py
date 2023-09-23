from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    super_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    # Definition of the one-to-many relationship with HeroPower
    powers = db.relationship('HeroPower', backref='hero')

class HeroPower(db.Model):
    __tablename__ = 'heroes_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id')) 
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))  
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    @validates('strength')
    def validate_strength(self, key, value):
        allowed_strengths = ['Strong', 'Weak', 'Average']
        if value not in allowed_strengths:
            raise ValueError("Invalid strength. Allowed values are 'Strong', 'Weak', 'Average'.")
        return value

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    @validates('description')
    def validate_description(self, key, value):
        if not value:
            raise ValueError("Description is required.")
        if len(value) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value

    # Define a one-to-many relationship with HeroPower
    heroes = db.relationship('HeroPower', backref='power')
