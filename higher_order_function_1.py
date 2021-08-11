# Practice with map
# Fill out the rest of the map functions.
# You can define additional functions if you need to.
# (a) ["apple", "orange", "pear"] => (5, 6, 4)  (length)
# (b) ["apple", "orange", "pear"] => ("APPLE", "ORANGE", "PEAR")  (uppercase)
# (c) ["apple", "orange", "pear"] => ("elppa", "egnaro", "raep")  (reversed)
# (d) ["apple", "orange", "pear"] => ("ap", "or", "pe")  (first two letters)

m_array = ["apple", "orange", "pear"]
def upper(word):
    return word.upper()
def reverse(word):
    return word[::-1]
def first_two(word):
    return word[0:2:1]
a = map(len, m_array)
b = map(upper, m_array)
c = map(reverse, m_array)
d = map(first_two, m_array)

print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))



# Practice with filter
# Fill out the rest of the filter functions.
# You can define additional functions if you need to.
# (a) range(100) => (0, 3, 6, 9, ...)  (div by 3)
# (b) range(100) => (0, 5, 10, 15, ...)  (div by 5)
# (c) range(100) => (0, 15, 30, 45, ...)  (div by 15)
# (d) range(100) => (1, 2, 4, 7, 8, 11, 13, 14, 16, 17, ...)  (not div by 3 and not div by 5)

a = filter(lambda val: val % 3 == 0, range(100))
# b = filter(???, ???)
# c = filter(???, ???)
# d = filter(???, ???)
print(tuple(a))