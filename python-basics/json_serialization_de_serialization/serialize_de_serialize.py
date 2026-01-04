import json


def serialize_obj(person:dict) -> str:
    # Serialize the object
    person_str= json.dumps(person)
    return person_str

def de_serialize_str(json_str:str) -> dict:
    # Deserialize the json string to object
    person_dict = json.loads(json_str)
    return person_dict

if __name__ == "__main__":
    person = {
        "first_name":"John",
        "last_name":"Rick",
        "date_of_birth": "1987-01-01",
        "age": 34,
        "isLive": True,
        "address" : {
            "address_line1":"1234 first street",
            "address_line2":"1001",
            "city":"Irving",
            "state":"Tx",
            "zip":7666
        },
        "interests":[
            "SKING",
            "TENNIS",
            "TRAVEL"
            ]
    }
    
    #print(person)
    json_str = serialize_obj(person)
    print("--Serialized Dictionary to json string--")
    print(json_str)

    print("--Deserialized Dictionary--")
    person_dict = de_serialize_str(json_str)
    print(person_dict)