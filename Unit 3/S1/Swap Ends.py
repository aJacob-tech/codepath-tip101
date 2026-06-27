#Understand: We want to swap the beg and end of a word, for example boat to toab
#Inputs: String, Output:String
#Plan: We want to first def a func that accepts a string var, then we call the end of the string, and then the middle and beg, then return to function
#Edge cases: integers, empty strings

def swap_ends(my_str):
   return my_str[-1] + my_str[1:-1] + my_str[0] 
   
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
