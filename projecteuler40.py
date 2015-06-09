# Project Euler 40
# Champernowne's Constant

import math

def main():
	frac = '1'
	product = 1
	number = 1

	while len(frac) < 1000000:
		number += 1
		frac += str(number)

	for i in range(0, 7, 1):
		product *= int(frac[int(math.pow(10,i)) - 1])

	print product


if __name__ == '__main__':
	main()