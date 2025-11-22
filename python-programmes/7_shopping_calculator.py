"""
Build a shopping calculator. 
Ask the user to input the price of an item and quantity they want to buy. 
Calculate the total cost and display it with proper formatting. 
Handle the fact that input comes as string.
"""
from decimal import Decimal

def calculate_item_total_price(item_price,item_quantity) :
    return item_price*item_quantity

if __name__ == "__main__" :
    print("Shopping Calculator Starts")
    item_name = input("Enter Item Name :")
    item_price = Decimal(input("Enter Item Price :"))
    item_quantity = int(input("Enter Item Quantity :"))

    item_total_price = calculate_item_total_price(item_price,item_quantity)
    print(f"Total Price of {item_name} is  : {item_total_price}")
    print("Shopping Calculator Ends")