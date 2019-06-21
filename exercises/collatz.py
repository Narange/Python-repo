import sys


def print_collatz_sequence(input_number):

    number = int(input_number)
    print(number)
    peak = number  # highest value reached in this sequence

    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        if number > peak:
            peak = number
        print(round(number))

    print(f"The Collatz sequence for {input_number} peaked at value {round(peak)}")


try:
    print_collatz_sequence(int(sys.argv[1]))
except IndexError:
    print("Provide one argument: an int for which to step through the Collatz sequence")
