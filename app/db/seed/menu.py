from faker import Faker
from app.models.category import CategoryModel
from app.models.menu import MenuModel
from sqlalchemy.orm import Session
import random

fake = Faker()

def seed_menus(db : Session , n=10):
    if db.query(MenuModel).count() > 0:
        return

    categories = db.query(CategoryModel).all()
    menus = []

    for _ in range(n):
        menu = MenuModel(
            title=fake.word().capitalize(),
            price=round(random.uniform(5.0, 50.0), 2),
            description=fake.sentence(),
            inventory=fake.random_int(1,100),
            category_id=random.choice(categories).id_category
        )
        menus.append(menu)

    db.add_all(menus)
    db.commit()