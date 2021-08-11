"""Generate an infinite stream of successively larger random lists."""
import helper_2
def generate_cases():
    count = 1
    while True:
        
        yield helper_2.random_list(count)
        count = count + 1
    
        
# if __name__ == '__main__':
#     for case in generate_cases():
#         if len(case) > 10:
#             break
#         print(case)

g = generate_cases()
print(next(g))
print(next(g))