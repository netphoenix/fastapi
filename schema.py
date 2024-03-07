from pydantic import BaseModel, ConfigDict

class UserAdd(BaseModel):
    name: str
    age: int
    phone: str|None = None

class USer(UserAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UserId(BaseModel):
    id: int