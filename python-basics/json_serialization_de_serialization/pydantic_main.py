from pydantic import BaseModel
from person import Person
from address import Address

def serialize_obj(person_obj:Person) -> str:
    return person_obj.model_dump_json(indent=4)
    
def deserialize_str(json_str:str) -> Person:
    return Person.model_validate_json(json_str)

if __name__ == "__main__":
    
    address = Address(
        address_line1="1234 main street",
        # This key is optional
        address_line2="1093",
        city="Irving",
        state="TX",
        zip=12345
        )
    
    
    person = Person(
        first_name="John",
        last_name="Mark",
        date_of_birth="1980-01-01",
        age=56,
        isLive=True,
        address=address,
        interests=["SKING", "TENNIS"]
        )
    
    person_obj = Person.model_validate(person)
    print("--Person Object--")
    print(person_obj)

    person_str = serialize_obj(person_obj)
    print("--Person Object Serialized--")
    print(person_str)

    person_obj = deserialize_str(person_str)
    print("--Person Object Deserialized--")
    print(person_obj)