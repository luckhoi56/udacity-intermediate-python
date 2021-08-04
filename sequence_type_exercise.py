"""Swap the keys and values in a mapping."""

def swap_keys_and_values(d):
    for key,value in d.items():
        print(key,value)
        key,value=value,key
        print(key,value)
    return d

a={"a":"leaf","b":"mouse"}
a = swap_keys_and_values(a)
print(a)