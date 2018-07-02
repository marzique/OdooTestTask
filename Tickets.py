import itertools

# calculate all "unique" combinations
def calculate_combinations(combinations, N, Sum):
    lucky_tickets = []
    for combination in combinations:
        first_half = combination[:N]
        second_half = combination[N:]
        first_sum = 0
        second_sum = 0

        for char1 in first_half:
            first_sum += int(char1)

        for char2 in second_half:
            second_sum += int(char2)

        if first_sum == second_sum == Sum:
            lucky_tickets.append(combination)

    return lucky_tickets

# generate all possible combinations of N digits
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
        lucky_combinations = calculate_combinations(lis, N, Sum)
        print(len(lucky_combinations))

    else:
        print("wrong input string")

else:
    print("wrong input string")


