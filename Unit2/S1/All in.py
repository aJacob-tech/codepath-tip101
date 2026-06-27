def all_in(a, b):
    for i in a:          # check every element in a
        for x in b:      # search for i in b
            if i == x:
                break    # found i in b, move to next i
        else:
            # inner loop finished without a break, meaning i was never found in b
            return False
    # every i was found in b
    return True

lst_1 = [1, 2,]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))
