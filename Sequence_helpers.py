import random
import string

# dicts to limit combinations
letters = {}
pairs = {}
triples = {}

# get random 3 lowercase letters as a string
def random_triple():
    return ''.join(random.choice(string.ascii_lowercase) for x in range(3))


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


# fill triples
def triples_counter(triple):
    if triple in triples:
        triples[triple] += 1
    else:
        triples[triple] = 1


# loop through each 3 letters with 1 letter shift
def scan_loop_triples(s):
    for i, j, k in zip(s[0:], s[1:], s[2:]):
        triples_counter(i + j + k)


# loop through each 3 letters with 1 letter shift
def scan_loop_pairs(s):
    for x, y in zip(s[0:], s[1:]):
        pairs_counter(x + y)


def scan_loop(s):
    for a in s:
        letters_counter(a)