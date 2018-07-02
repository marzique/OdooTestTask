import itertools

def calculate_combinations(list1, list2):
    pass

def generate_list(dimensions):
    combinations = []
    for i in itertools.product(range(10), repeat=dimensions):
        number = ''.join(map(str, i))
        combinations.append(number)
    return combinations

inputs = input("Enter input string:").split()

if inputs[0].isdigit() and inputs[1].isdigit():

    N = int(inputs[0])
    Sum = int(inputs[1])
    if 1 <= N <= 50 and 1 <= Sum <+ 1000:
        lis = generate_list(2*N)
        print(lis)


    else:
        print("wrong input string")

else:
    print("wrong input string")


