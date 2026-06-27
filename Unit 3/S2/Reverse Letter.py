'''
Inputs: string
Outputs: new string
Understand: we will take in a str, and reverse only the letters in the str, the - will remain the same, then we will return it into a new string
Plan: def func, new str var, for loop to loop char in str, and then append into new str, and then return
Edge Cases:
'''


def reverse_only_letters(s):
    new_str = ""
    result = ""
    j=0
    for i in s:
        if i.isalpha():
            new_str += i
    new_str = new_str[::-1]
    for i in s:
        if not i.isalpha():
            result += i
        else: 
            result += new_str[j]
            j += 1
    
    return result

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
        
