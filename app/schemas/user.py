from typing import List
from pydantic import BaseModel, ConfigDict
from app.schemas.reservation import ReservationItemResponseSchema

"""
Input and output are different, password is not returned in the response
"""

class UserSchema(BaseModel):
    name: str
    email: str
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)

class UserResponseSchema(BaseModel):
    name: str
    email: str
    items: List[ReservationItemResponseSchema] = []

    model_config = ConfigDict(from_attributes=True)
