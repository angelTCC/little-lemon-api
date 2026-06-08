from faker import Faker
import random
from app.models.reservation import ReservationModel, ReservationItemModel
from app.models.user import UserModel
from app.models.menu import MenuModel
from sqlalchemy.orm import Session

fake = Faker()

def seed_reservations(db: Session, n=15):
    if db.query(ReservationModel).count() > 0:
        return

    users = db.query(UserModel).all()
    menu_items = db.query(MenuModel).all()

    statuses = ["pending", "confirmed", "cancelled"]

    for _ in range(n):
        reservation = ReservationModel(
            client_id=random.choice(users).id_user,
            status=random.choice(statuses)
        )

        db.add(reservation)
        db.commit()
        db.refresh(reservation)

        # 1–3 items por reserva
        for _ in range(random.randint(1, 5)):
            item = ReservationItemModel(
                reservation_id=reservation.id_reservation,
                menu_id=random.choice(menu_items).id_menu,
                quantity=random.randint(1, 5)
            )
            db.add(item)

        db.commit()