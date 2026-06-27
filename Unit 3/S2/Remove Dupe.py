'''
Inputs: Lst of int
Outputs: new lst of int
Understand: have a lst of int, where we have to remove duplicated numbers and return a new list
Plan: we will create a new list, and create index var, and use a while loop to loop through nums and append the ints into the new lst, then return new lst
Implement: New lst, index var, while loop, if statement, i += 1 to go to next index, return statement when done
Edge Cases: strings in new lst, empty lst, none, duplicated nums in new lst
'''
def remove_duplicates(nums):
    new_lst = []
    i = 0
    while i < len(nums):
        if nums[i] not in new_lst:
            new_lst.append(nums[i])
        i += 1
    return new_lst

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

