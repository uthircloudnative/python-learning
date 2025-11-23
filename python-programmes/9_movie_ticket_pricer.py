"""
Build a movie ticket pricing system. 
Based on age, determine ticket price: 
 children (≤12) pay $8, 
 teens (13-17) pay $12, 
 adults (18-64) pay $15, 
 and seniors (≥65) pay $10. 
Also add a discount day (Wednesday) where everyone gets $3 off.
"""

import datetime

def get_current_day() :
    today = datetime.datetime.now()
    today_name = today.strftime('%A')
    print(f"Current Day is : {today_name}")
    return today_name

def calculate_ticket_price(age) :
    if age <= 12 :
      ticket_price = 8
    elif age >= 13 and age <= 17 :
      ticket_price = 12
    elif age >= 18 and age <= 64 :
      ticket_price = 15
    elif age > 64 :
      ticket_price = 10

    today = get_current_day()
    if today == "Wednesday" :
      ticket_price = ticket_price - 3

    return ticket_price

if __name__ == "__main__" :
    print("Movie Ticket Pricer Starts")
    age = int(input("Enter your Age :"))
    ticket_price = calculate_ticket_price(age)
    print(f"Your Movie Ticket Price is : ${ticket_price}")
    print("Movie Ticket Pricer Ends")