"""

Create a properly formatted program that calculates the area of different rooms in a house. 
Define variables for length and width of 3 rooms (living_room, bedroom, kitchen) and calculate their areas. 
Use proper variable naming and formatting.

"""

def calculate_area(room_name, length, width):
    print(f"Calculating Area of ${room_name}")
    return (length * width)

if __name__ == "__main__" :
    print("Calculate Area Starts")
    room_name = 'living_room'
    room_area = 0
    room_area = calculate_area(room_name,70,10)
    print(f"{room_name} area is {room_area}")
    room_name = 'bedroom'
    room_area = calculate_area(room_name,20,10)
    print(f"{room_name} area is {room_area}")
    room_name = 'kitchen'
    room_area = calculate_area(room_name,10,10)
    print(f"{room_name} area is {room_area}")

    print("Calculate Area Ends")