# Manipulating Lists and Tuples
# Write a function to produce the next layer of Pascal's triangle
# Each layer is one larger than the previous layer, and each element in
# the new layer is the sum of the two elements above it in the previous
# layer. For example, `(1, 3, 3, 1) -> (1, 4, 6, 4, 1)`.
#
# Hint: What does the expression `zip(row + (0,), (0,) + row)` produce?

def add_layer(row):
    # Add a layer to Pascal's triangle.
    # Each layer should be a tuple.
    print(type(row))
    zipped_row = zip(row + (0,), (0,) + row)
    final_row = list(map(sum,zipped_row))
    return final_row
    
    
pascals_triangle = [
    (1,),
    (1, 1),
    (1, 2, 1),
    (1, 3, 3, 1),
]

# Add a few layers, just to check.
for n in range(5):
    m_length = len(pascals_triangle)
    temp = add_layer(pascals_triangle[-1])
    pascals_triangle.append(temp)
    print(n)

