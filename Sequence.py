import random
import string

# dicts to limit combinations
letters = {}
pairs = {}
triples = {}

# main million length string to output
million_sting = ""


# get random 3 lowercase letters as a string
def random_triple():
    return ''.join(random.choice(string.ascii_lowercase) for x in range(3))


# loop through each 3 letters with 1 letter shift
def scan_loop(s):
    for i, j, k in zip(s[0:], s[1:], s[2:]):
        print(i + j + k)

# same as above but backwards
def new_combinations(word):
    for i, j, k in zip(word[-1:], word[-2:], word[-3:]):
        print(k + j + i)

# fill letters dict
def letters_counter(char):
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1

# fill pairs
def pairs_counter(pair):
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

# fill
def triples_counter(triple):
    if triple in triples:
        triples[triple] += 1
    else:
        triples[triple] = 1


# generate 1,000,000 len random string temporary
for tr in range(333333):
    million_sting += random_triple()

million_sting += random.choice(string.ascii_lowercase)

print(million_sting)
print(len(million_sting))

for a in million_sting:
    letters_counter(a)



print(letters)
# print(pairs)
# print(triples)
# new_combinations(word)

