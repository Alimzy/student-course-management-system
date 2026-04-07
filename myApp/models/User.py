from models.Role import Role
from pydantic import BaseModel

class User(BaseModel):
    id:str
    name: str
    email:str
    role:Role

