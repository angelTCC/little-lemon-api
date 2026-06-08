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
    reservation_id: int
    menu_id: int
    quantity: int

    model_config = ConfigDict(from_attributes=True)


# == SCHEMAS FOR RESERVATION ==

class ReservationSchema(BaseModel):
    client_id: int
    status: str

class ReservationResponseSchema(BaseModel):
    client_id: int
    status: str

    items: List[ReservationItemResponseSchema] = []

