"""Generate an infinite stream of successively larger random lists."""
import helper_2
def generate_cases(size):
    while True:
        yield helper_2.random_list(size)
    
        
if __name__ == '__main__':
    for case in generate_cases(10):
        if len(case) > 10:
            break
        print(case)