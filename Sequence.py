import random
import string

letters = {"a": 1, "b": 2}
pairs = {}
triples = {}
mill_sting = ""


# get random 3 lowercase letters as a string
def random_triple():
    return ''.join(random.choice(string.ascii_lowercase) for x in range(3))


# loop through each 3 letters with 1 letter shift
def scan_loop(s):
    for i, j, k in zip(s[0:], s[1:], s[2:]):
        print(i + j + k)


def letters_counter(char):
    if char in letters:
        letters[char] += 1
        print(letters[char])
    else:
        letters[char] = 1
        print(char + " added to dict")


def pairs_counter(pair):
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1


def triples_counter(triple):
    if triple in triples:
        triples[triple] += 1
    else:
        triples[triple] = 1

