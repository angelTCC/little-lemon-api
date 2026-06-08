from enum import Enum
from pydantic import BaseModel, ConfigDict
from typing import List

"""
"""

#  == SCHEMAS FOR RESERVATION ITEM ==

class ReservationItemSchema(BaseModel):
    reservation_id: int
    menu_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)

class ReservationItemResponseSchema(BaseModel):
    id_item: int
    reservation_id: int
    menu_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


# == SCHEMAS FOR RESERVATION ==

class ReservationStatus(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class ReservationSchema(BaseModel):
    client_id: int
    status: ReservationStatus

class ReservationResponseSchema(BaseModel):
    client_id: int
    status: ReservationStatus
    id_reservation: int

    items: List[ReservationItemResponseSchema] = []

