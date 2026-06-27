def common_keys(dict1, dict2):
    my_lst = []
    for k, v in dict1.items():
        if k in dict2:
            my_lst.append(k)
    return my_lst
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
