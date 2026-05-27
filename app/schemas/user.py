from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    name: str
    email: str
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)