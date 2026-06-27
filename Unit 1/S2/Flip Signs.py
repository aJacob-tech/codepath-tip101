def flip_sign(lst):
    flipped_lst = []
    for i in lst:
        flipped_lst.append(i*-1)
    return flipped_lst

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

#Understand: inputs: list, outputs: new list, edge cases: strings, none, empty list, list with 0
#Plan: Def the func, create new_list, for loop to append into the new list, then return new list, and then call it

