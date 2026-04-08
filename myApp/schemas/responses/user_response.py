from typing import Optional

from myApp.models.Role import Role
from pydantic import BaseModel

class UserResponse(BaseModel):
    name: str
    email:str
    role:Role

