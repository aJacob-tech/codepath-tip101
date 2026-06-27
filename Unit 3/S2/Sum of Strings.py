'''
Inputs: lst of str 
Outputs: Int
Understand: create a func that takes a lst of str, and then add up the strings and get the sum and return an int
Plan: create def func, sum var, for loop to loop lst, add up the str and convert to int, return sum var
Edge Cases: Empty lst, non integer strings

'''
def sum_of_number_strings(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

