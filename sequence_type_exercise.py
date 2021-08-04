d = {"one": 1, "two": 2, "three": 3}
print(d["two"])
#2
d["three"] = 5
## d = {"one": 1, "two": 2, "three": 5}
del d["one"]
print(len(d))
#2
d["four"] = 11
## d = {"one": 1, "two": 2, "three": 5,"four":8}
# print(d.get("three", "four"))
print(d)
#5
# print(d.get("three", d["four"]))
#5
# print(max(d.values()))
# #8
# print(min(d))
# #four
# print(d.pop("four", 4))
# #8
# print(d.pop("one", d["two"]))
# #
# print(d.pop("two"))
# for key, value in d.items():
#     print(key * value)