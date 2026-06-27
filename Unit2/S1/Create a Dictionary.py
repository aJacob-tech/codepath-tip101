def create_dictionary(keys, values):
    result = {} # start with an empty dictionary
    for i in range(len(keys)): # len(keys): counts how many elements are in keys list. Then range generates numbers based on the length
        result[keys[i]] = values[i] # key[i]: the index of the key, value[i]: index of the value, then it adds to the result dictionary
    return result # return the completed dictionary back

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

print(create_dictionary(keys, values))