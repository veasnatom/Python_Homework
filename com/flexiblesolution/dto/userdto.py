from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserDto(BaseModel):
    id : Optional[int]
    name : Optional[str]
    email : Optional[str]
    phone : Optional[str]
    password : Optional[str]
    created_at : Optional[datetime]
    updated_at : Optional[datetime]
    class Config:
        orm_mode = True