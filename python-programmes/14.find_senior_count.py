"""
Number Of Senior Citizens
You are given a 0-indexed array of strings p, containing information about a given passenger consists of their phone number (first 10 characters), gender (11th character), age (12th and 13th characters), and seat assignment (last two characters).

Return the number of passengers who are strictly more than 60 years old.
"""

if __name__ == "__main__":
    p =  ["7823190130M7511", "6868346633F3422", "9921362780M5644", "9954362340M6707"]
    
    senior_count = 0
    for person in p:
        age = int(person[-4:-2])
        print(age)
        if(age > 60):
            senior_count += 1
    print(senior_count)  # Output: 3