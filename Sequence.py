from Sequence_helpers import *


million_sting = ""

flag = True

while flag:
    # generate 999,999 len random string temporary
    for tr in range(333333):
        million_sting += random_triple()

    # 1,000,000
    million_sting += random.choice(string.ascii_lowercase)

    # fill in dicts
    scan_loop(million_sting)
    scan_loop_triples(million_sting)
    scan_loop_pairs(million_sting)

    if max(letters.values()) <= 40000 and max(pairs.values()) <= 2000 and max(triples.values()) <= 100 :

        flag = False
        print("The most frequent letter occured "  + str(max(letters.values())) + " times")
        print("The most frequent pair occured "  + str(max(pairs.values())) + " times")
        print("The most frequent triple occured "  + str(max(triples.values())) + " times")

