def max_difference(lst):
    max = lst[0]  # assume the first item is the largest to start
    min = lst[0]  # assume the first item is the smallest to start

    for i in lst:  # loop through every number in the list
        if max < i:      # if we find a number bigger than our current max...
            max = i      # ...update max to that number

        if min > i:      # if we find a number smaller than our current min...
            min = i      # ...update min to that number

    return max - min  # subtract min from max to get the biggest difference

lst = [5, 22, 8, 10, 2]
max_diff = max_difference(lst)  # calls the function and stores the result
print(max_diff)                 # prints 20  (22 - 2 = 20)

#Understand: Input:list, Outputs: difference of largest - smallest, Edge cases:Null, Strings, None, empty list, 
#Plan: def the fucn, for loop to get max and min, return difference, the call def
