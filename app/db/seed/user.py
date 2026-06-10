from faker import Faker
from app.models.user import UserModel
from sqlalchemy.orm import Session

from app.db.hash import Hash

fake = Faker()

def seed_users(db: Session, n=10):
    if db.query(UserModel).count() > 0:
        return

    users = []

    for _ in range(n):
        name = fake.first_name()
        user = UserModel(
            name=name,
            email=fake.unique.email(),
            hashed_password= Hash.get_password_hash(name) #fake.password(length=12)
        )
        users.append(user)

    db.add_all(users)
    db.commit()