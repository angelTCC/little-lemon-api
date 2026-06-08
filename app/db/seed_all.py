from app.db.seed.category import seed_categories
from app.db.seed.user import seed_users
from app.db.seed.menu import seed_menus
from app.db.seed.reservation import seed_reservations

from app.db.session import SessionLocal

def run_seed():
    db = SessionLocal()

    try:
        seed_categories(db)
        seed_users(db, n=20)
        seed_menus(db, n=50)
        seed_reservations(db, n=30)

        print("🌱 Faker seed completed!")

    except Exception as e:
        db.rollback()
        print("❌ Error:", e)

    finally:
        db.close()