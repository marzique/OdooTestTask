import random
import string
from Sequence_helpers import *

million_sting = ""
condition_flag = True

while condition_flag:

    # 1,000,000
    million_sting += ''.join(random.choice(string.ascii_lowercase) for _ in range(1000000))

    # fill in dicts
    scan_loop(million_sting)
    scan_loop_triples(million_sting)
    scan_loop_pairs(million_sting)

    # check for hypothetical situation of exceeding the limits
    if max(letters.values()) <= 40000 and max(pairs.values()) <= 2000 and max(triples.values()) <= 100 :

        condition_flag = False
        print(million_sting)
        print("The most frequent letter occured "  + str(max(letters.values())) + " times")
        print("The most frequent pair occured "  + str(max(pairs.values())) + " times")
        print("The most frequent triple occured "  + str(max(triples.values())) + " times")

