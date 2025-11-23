"""
Create a multiplication table generator. 
Generate and display the multiplication table for number 7 (from 7×1 to 7×10). 
If the result is greater than 50, display "HIGH" next to it, otherwise display "LOW"

"""
def create_multiplication_table(multiplier, iteration_limit) :
    for i in range(1, iteration_limit + 1) :
      print(f"{multiplier} * {i} = {multiplier*i} --> {'HIGH' if multiplier*i > 50 else 'LOW'}")

if __name__ == "__main__" :
    print("Multiplication table Starts")
    multiplier = int(input("Enter Multiplier Number :"))
    iteration_limit = int(input("Enter table range :"))
    create_multiplication_table(multiplier,iteration_limit)
    print("Multiplication table Ends")