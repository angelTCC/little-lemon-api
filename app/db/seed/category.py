from app.models.category import CategoryModel

def seed_categories(db):
    if db.query(CategoryModel).count() > 0:
        return

    categories = [
        CategoryModel(name="Food"),
        CategoryModel(name="Drinks"),
        CategoryModel(name="Desserts"),
        CategoryModel(name="Fast Food"),
    ]

    db.add_all(categories)
    db.commit()