from pydantic import BaseModel

class Address(BaseModel):
    address_line1: str
    # This key is optional
    address_line2: str | None = None
    city: str
    state: str
    zip: int