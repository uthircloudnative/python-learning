age = input("Enter user age :", )
age = int(age)  # Convert input to integer
message = "You are a toddler." if age <= 5 else "You are not a toddler."
print(message)
