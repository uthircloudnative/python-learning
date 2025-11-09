"""
Create a grade analyzer program. 
Given test scores [85, 92, 78, 96, 88, 73, 90], 
find and display the highest score, 
lowest score, and determine if a student with score 85 passed (passing grade is 75)

"""

def find_highest_score(mark_list):
   return max(mark_list)

def find_lowest_score(mark_list):
    return min(mark_list)

def find_grade(mark_list):
    for mark in mark_list :
        #print(f"Mark ${mark}")
        if mark >= 75 :
            print(f"Mark is ${mark} and its Pass Grade")
        else :
            print(f"Mark is ${mark} and its Fail Grade")

if __name__ == "__main__" :
    print("Grade Analyzer starts")
    mark_list = [85, 92, 78, 96, 88, 73, 90]
    max_mark = find_highest_score(mark_list)
    print(f"Max Mark is ${max_mark}")
    min_mark = find_lowest_score(mark_list)
    print(f"Min Mark is ${min_mark}")
    find_grade(mark_list)
    print("Grade Analyzer Ends")