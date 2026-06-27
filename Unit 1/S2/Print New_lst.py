def doubled(lst):
    new_lst = [] #this creates a empty list
    for i in lst:
        new_lst.append(i * 2) # this adds the double value of lst into the new list, with append
    return new_lst #return the list 

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)