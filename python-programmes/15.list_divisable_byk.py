"""
Given a list of lists t containing integers, and a positive integer k, the task is to return a new list of lists containing only those sublists in which every element is divisible by k. The order of sublists in the resulting list should be the same as their original order in the input list.

Example One
{
"t": [[1, 2, 3], [2, 4, 6], [3, 10, 11]],
"k": 2
}
"""

def divisible_by_k(t, k):
    result = []
    for in_list in t:
        is_dvisible = True
        print(in_list)
        for num in in_list:
            print(num)
            if num%2 != 0:
                is_dvisible = False
                print("Not Divisible", num)
                break
        print("Divisible", is_dvisible)
        if(is_dvisible):
            result.append(in_list)
            print("Result", result)

    return result
              
    

if __name__ ==  "__main__":
    t = [[1, 2, 3], [2, 4, 6], [3, 10, 11]]
    k = 2
    print(divisible_by_k(t, k))  # Output: [[2, 4, 6]]

