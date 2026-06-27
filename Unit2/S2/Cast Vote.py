def cast_vote(votes, candidate):
    if candidate in votes: #the dict is votes, and candidate is the key so, it is saying if the key is in the dict then do line 3
        votes[candidate] += 1 # This access the values through the key and + 1
    else:
        votes[candidate] = 1 # this adds a new key with value of 1


votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
