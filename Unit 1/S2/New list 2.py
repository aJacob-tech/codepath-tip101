def doubled(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i*2)
    return new_lst
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

#Understand: inputs: list, Output: new list, edge cases: strings, none, empty list
#Plan: def the func, create an empty list, for loop in order to add doubled number into the new list, then return new list, then we print
