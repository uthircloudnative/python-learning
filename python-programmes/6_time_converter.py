"""

Create a time converter program. 
Given a total number of seconds (e.g., 7265), 
convert it to hours, minutes, and remaining seconds. 
Use floor division and modulus operators. 
Also calculate the absolute difference between two time periods.

"""

def calculate_hours_minutes(seconds) :
    hours = seconds//(60*60)
    #print(f"Total Hours : {hours}")

    minutes = seconds%(60*60)

    actual_minutes = minutes//60
    actual_seconds = minutes%60
    #print(f"Total Minutes : {actual_minutes}")
    #print(f"Total Seconds : {actual_seconds}")

    print(f"Total Time : {hours} hours : {actual_minutes} minutes : {actual_seconds} seconds")

def calculate_time_difference(seconds1, seconds2) :
    return abs(seconds1 - seconds2)

if __name__ == "__main__" :
    print("Time Converter Starts")
    calculate_hours_minutes(3600)
    #hours_by_diviosn = calulate_hours(7265)
    seconds1 = 7265
    seconds2 = 5400
    time_diff_in_seconds = calculate_time_difference(seconds1,seconds2)
    print(f"Time Difference in Seconds : {time_diff_in_seconds}")
    # Print Time difference in Hours, Minutes, Seconds
    calculate_hours_minutes(time_diff_in_seconds)
    #print(f"Hours by Division : {hours_by_diviosn}")
    print("Time Converter Ends")