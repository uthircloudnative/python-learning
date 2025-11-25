"""
Build a seating chart generator for a small theater. 
Create a 5-row by 8-seat layout, 
displaying each seat as "Row-Seat" format (e.g., "R1-S1", "R1-S2"). 
Mark seats R3-S4 and R3-S5 as "RESERVED".
"""

def seat_chart_creator(number_of_rows,number_of_seats) :
    row_num = 1
    for row_num in range(1,number_of_rows+1) :
      #print()
      seat_num = 1
      row = "R" + str(row_num)
      #print(row)
      row_str = ""
      for seat_num in range(1,number_of_seats+1) :
          seat = "S" + str(seat_num)
          row_seat = row + "-" + seat
          #print(row_seat)
          if seat_num == number_of_seats :
            if row_num == 3 and (seat_num ==5) :
              row_seat += " (RESERVED)"
            row_seat = row_seat
          else :
            if row_num == 3 and (seat_num ==4) :
              row_seat += " (RESERVED)"
            row_seat += ","
          print(row_seat, end=" ")
        #print(f"{row}-{seat}")
      print()

if __name__ == "__main__" :
    print("Seating Chart Generator Starts")
    number_of_rows = int(input("Enter Number of Rows :"))
    number_of_seats = int(input("Enter Number of Seats :"))
    seat_chart_creator(number_of_rows,number_of_seats)
    #print("Seating Chart Generator Ends")