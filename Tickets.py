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

        if first_sum == second_sum == Sum/2:
            lucky_tickets.append(combination)

    return lucky_tickets

# generate all possible N digit combinations
def generate_list(dimensions):
    combinations = []
    for i in itertools.product(range(10), repeat=dimensions):
        number = ''.join(map(str, i))
        combinations.append(number)
    return combinations

def main():
    inputs = input("Enter input string:").split()

    # ensure valid input
    if len(inputs) >= 2:
        if inputs[0].isdigit() and inputs[1].isdigit():

            N = int(inputs[0])
            Sum = int(inputs[1])
            if 1 <= N <= 50 and 1 <= Sum <+ 1000:
                lis = generate_list(2*N)
                lucky_combinations = calculate_combinations(lis, N, Sum)
                # print(lucky_combinations)
                print(len(lucky_combinations))

            else:
                print("wrong input string")
        else:
            print("wrong input string")

    else:
        print("wrong input string")


if __name__ == "__main__":
    main()


