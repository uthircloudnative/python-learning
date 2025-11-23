"""
Create a weather recommendation system. 
Ask for temperature, then use ternary operator to suggest: "Wear a jacket" if temp < 60, 
otherwise "T-shirt weather". 
Also determine if it's "Hot day" (>80) or "Comfortable".

"""

if __name__ == "__main__" :
    print("weather recommendation system Starts")
    temperature = int(input("Enter temperature :"))
    suggestion = "Wear a jacket" if temperature < 60 else "T-shirt weather"
    print(suggestion)
    type_of_day = "Hot day" if temperature > 80 else "Comfortable"
    print(type_of_day)
    print("weather recommendation system Ends")