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