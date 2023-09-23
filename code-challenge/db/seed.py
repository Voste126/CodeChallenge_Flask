# from app import app, db
# from app.models import Hero 
# from app.models import Power
# from app.models import HeroPower
# import random

# print("🦸‍♀️ Seeding powers...")

# powers_data = [
#     {"name": "super strength", "description": "gives the wielder super-human strengths"},
#     {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
#     {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
#     {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
# ]

# for power_info in powers_data:
#     Power(**power_info).save()

# print("🦸‍♀️ Seeding heroes...")

# heroes_data = [
#     {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
#     {"name": "Doreen Green", "super_name": "Squirrel Girl"},
#     {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
#     {"name": "Janet Van Dyne", "super_name": "The Wasp"},
#     {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
#     {"name": "Carol Danvers", "super_name": "Captain Marvel"},
#     {"name": "Jean Grey", "super_name": "Dark Phoenix"},
#     {"name": "Ororo Munroe", "super_name": "Storm"},
#     {"name": "Kitty Pryde", "super_name": "Shadowcat"},
#     {"name": "Elektra Natchios", "super_name": "Elektra"}
# ]

# for hero_info in heroes_data:
#     Hero(**hero_info).save()

# print("🦸‍♀️ Adding powers to heroes...")

# strengths = ["Strong", "Weak", "Average"]
# heroes = Hero.objects.all()

# for hero in heroes:
#     for _ in range(random.randint(1, 3)):
#         power = random.choice(Power.objects.all())
#         HeroPower(hero=hero, power=power, strength=random.choice(strengths)).save()

# print("🦸‍♀️ Done seeding!")

# if __name__ == '__main__':
#     with app.app_context():
        

