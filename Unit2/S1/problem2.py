#Understand: Create a Func that pairs a list of keys and values
#Plan: def func,empty dict, for loop to see range(len(keys)), then append keys = values to the empty dict, return dict, then add inputs, and print
#edge cases: check if empty, assume keys and values are same length

def create_dictionary(keys, values):
    seen = {}
    for i in range(len(keys)):
        seen[keys[i]] = values[i]
    return seen

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

print(create_dictionary(keys, values))
        
