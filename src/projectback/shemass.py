from pydantic import BaseModel

class StatusResponse(BaseModel):
    status: str

class UserResponse(BaseModel):
    username: str
    email: str
    full_name: str

class User(BaseModel):
    username: str
    email: str
    name: str
    password: str

class Pet(BaseModel):
    id: int
    name: str
    animal_type: str