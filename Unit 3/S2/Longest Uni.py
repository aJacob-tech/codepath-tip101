def longest_uniform_substring(s):
    length = 1
    i = 0
    maximum = 1
    while i < len(s):
        if s[i] == s[i-1]:
            length += 1
        else: 
            maximum = max(maximum, length)
            length = 1
        i += 1
        
    return max(maximum, length)


s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)



