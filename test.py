def merge_dict(dict_a,dict_b):
    return {**dict_a,**dict_b}

dict_1 = {"bitch":"a"}
dict_2 = {"fuck" :"b"}

print(merge_dict(dict_1,dict_2))