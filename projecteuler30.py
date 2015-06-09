# Project Euler 30
# Digit Fifth Powers

import math

def main():
	sum_of_fifths = 0
	sequence = []

	for x in range(10,1000000,1):
		if x == digit_sum(x):
			sequence.append(x)

	for i in sequence:
		sum_of_fifths += i

	print sum_of_fifths


def digit_sum(x):
	x_string = str(x)
	fifth_power_digit_sum = 0

	for i in range(0,len(x_string),1):
		fifth_power_digit_sum += math.pow(int(x_string[i]),5)

	return fifth_power_digit_sum


if __name__ == '__main__':
	main()