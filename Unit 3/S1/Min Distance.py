#Understand: Inputs:Lst, two strings, Outputs:Integer We have to see the min distance from word1 to word2




def min_distance(words, word1, word2):
    counter = 0
    
    for num in words:
        if num == word1:
            last1 = counter
        if num == word2:
            last2 = counter
        counter += 1
    return abs(last1 - last2)      
    '''
        if num in words[::-1]:
            word1 = counter
            word2 = counter
            return word2 - word1
        counter += 1
    '''
words = ["the", "quick", "brown", "fox", "jumped", "the"]

dist1 = min_distance(words, "quick", "jumped")
dist11 = min_distance(words[::-1], "quick", "jumped")
if dist1 > dist11:
    print(dist11)
else:
    print(dist1)

dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

        


    
        
