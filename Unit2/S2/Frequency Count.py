def count_occurrences(nums):
    my_dict = {} #Empty Dict
    for i in nums: # Gets all values in the List
        if i in my_dict: # if values are in dict
             my_dict[i] += 1 # then, adds to the value of the key
        else:
            my_dict[i] = 1 # else, if key not created then add key to = 1
    return my_dict
    
nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))