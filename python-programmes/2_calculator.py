"""
Build a simple calculator for a restaurant bill. 
Calculate the total cost when you order 3 pizzas at $12.50 each, 
2 drinks at $3.25 each, 
add 8% tax, and then add a 15% tip on the subtotal.

"""

from decimal import Decimal


def  calculate_item_price(item_name, quantity, price) :
    print(f"Item Name ${item_name}")
    item_quantity = Decimal(quantity)
    print(f"Quantity ${item_quantity}")
    item_price = Decimal(price)
    print(f"Price ${item_price}")
    item_total = item_quantity * item_price
    return round(item_total, 2)

def calculate_tax(toatl, tax) :
    return round((toatl * tax), 2)

def calculate_tip(toatl, tip_amount) :
    return round((toatl * tip_amount), 2)

if __name__ == "__main__":
    print("Calculator program starts")
    item_1_total = calculate_item_price('pizza', '3', '12.50')
    print(f"item_1_total ${item_1_total}")
    item_2_total = calculate_item_price('drinks', '2', '3.25')
    print(f"item_2_total ${item_2_total}")
    
    item_sub_total = item_1_total + item_2_total
    print(f"item_sub_total ${item_sub_total}")

    item_tax = calculate_tax(item_sub_total, Decimal('0.08'))
    print(f"item_total_tax ${item_tax}")

    total_tip_amount=calculate_tip(item_sub_total, Decimal('0.15'))
    print(f"total_tip_amount ${total_tip_amount}")

    total_price = item_sub_total + item_tax + total_tip_amount
    print(f"Total Price ${total_price}")
    print(f"Calculator program ends")