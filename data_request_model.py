from pydantic import BaseModel, validator, root_validator
from typing import Optional


class User(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    age: Optional[int] = 0

    @validator('phone_number')
    def parse_phone_number(cls, phone_number: str):
        return f'Phone: {phone_number} XXX'

 