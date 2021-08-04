"""Check whether a word is 'efficient' - if each letter can be drawn by a pencil without lifting."""
EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')

def is_efficient(letters):
    if(letters - EFFICIENT_LETTERS == set()):
        return True
    return False

print(is_efficient(set("BCD")))
print(set("BCDK")-EFFICIENT_LETTERS)