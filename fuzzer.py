"""Generate an infinite stream of successively larger random lists."""

def generate_cases():
    yield []
        
if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)