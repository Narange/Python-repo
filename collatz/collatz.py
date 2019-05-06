import sys

def print_collatz_sequence(input_number):

	number = int(input_number)
	print(number)
	peak = number #highest value reached in this sequence

	while number != 1:
		if number%2 == 0:
			number = number/2
		else:
			number = number*3 + 1

		if number > peak:
			peak = number

		print(round(number))

	print("The Collatz sequence for %s peaked at value %s" %(input_number, round(peak)))
#end def

print_collatz_sequence(int(sys.argv[1]))