# Project Euler 34
# Digit Factorials

import math

def main():
	total = 0

	for x in range(3,1000000,1):
		x_string = str(x)
		x_digits = []
		
		for i in range(0,len(x_string),1):
			x_digits.append(int(x_string[i]))

		digit_sum = 0
		for j in x_digits:
			digit_sum += math.factorial(j)

		if digit_sum == x:
			total += x

	print total


if __name__ == '__main__':
	main()