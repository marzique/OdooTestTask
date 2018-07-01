import random
import string

letters = {}
pairs = {}
triples = {}
mill_sting = ""


# get random 3 chars in string
def random_triple():
    return ''.join(random.choice(string.ascii_lowercase) for x in range(3))

mill_sting = random_triple() + random_triple() + random_triple() + random_triple()

# for letter in mill_sting:
#     if letter

print(mill_sting)

#
for i,j,k in zip(mill_sting[0:], mill_sting[1:], mill_sting[2:]):
    print(i,j,k)