'''
U: We have to see if the string typed has the same chars as name, and also number of a char as in name, it could be more.

Inputs: Two string
Outup: Boolean


P:
Define our function with name and typed as parameters
Initialize p_name and p_typed to 0

Loop while p_typed is less than the length of typed

    If p_name is less than the length of name AND current char of name equals current char of typed
        Increment p_name by 1
        Increment p_typed by 1

    Else if p_typed is greater than 0 AND current char of typed equals previous char of typed
        Increment p_typed by 1

    Else
        Return False

Return whether p_name equals the length of name
'''

def is_long_pressed(name, typed):
    namepoint = 0
    typedpoint = 0
    while typedpoint < len(typed):
        if namepoint < len(name) and typed[typedpoint] == name[namepoint]:
            namepoint += 1
            typedpoint +=1
        elif typedpoint > 0 and typed[typedpoint] == typed[typedpoint - 1]:
            typedpoint += 1
        else:
            return False
    return namepoint == len(name)

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
