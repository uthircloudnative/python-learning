from pydantic import BaseModel
from datetime import date
from address import Address

class Person(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    age: int
    isLive: bool | None = None
    address: Address
    interests: list[str]