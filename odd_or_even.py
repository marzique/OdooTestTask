def OddOrEven(number):
    if type(number) == int and number >= 1:
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")

    else:
        print("Wrong input")


OddOrEven(-1)
OddOrEven(0)
OddOrEven(1)
OddOrEven(2)
OddOrEven(123123123)
OddOrEven("string test")
OddOrEven(1.3)