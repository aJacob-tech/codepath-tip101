def get_last(lst):
    if lst == None:
        return None
    else:
        return lst[len(lst) - 1]
      
    
input = [3,1,6,7,5]

print(get_last(input))