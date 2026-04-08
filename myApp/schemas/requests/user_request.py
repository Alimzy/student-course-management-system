from myApp.models.Role import Role
from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    email:str
    role:Role

