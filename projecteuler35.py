# Project Euler 35
# Circular Primes
# Algorithm can actually be approved. I know that if the number 17 passes, then 71 does too
# so I don't actually have to run the algorithm on that number

import math

def main():
	circ_primes = []

	for x in range(0, 1000000, 1):
		if x not in circ_primes:
			check_prime = 0
			numbers = DigitRotation(x)

			for n in numbers:
				if IsPrime(n):
					check_prime += 0
				else:
					check_prime += 1

			if check_prime == 0:
				for n in numbers:
					circ_primes.append(n)

	print circ_primes
	print len(circ_primes)


def DigitRotation(n):
	n_string = str(n)
	n_digits = []
	numbers = []

	for i in range(0, len(n_string), 1):
		n_digits.append(n_string[i])

	for i in range(0, len(n_digits), 1):
		num = ""

		for j in range(i, len(n_digits), 1):
			num += n_digits[j]

		for j in range(0, i, 1):
			num += n_digits[j]

		if int(num) not in numbers:
			numbers.append(int(num))

	return numbers


def IsPrime(n):
	n = abs(int(n))

	if n < 2:
		return False
	if n == 2:
		return True

	for x in range (2, int(math.sqrt(n)+1), 1):
		if n % x == 0:
			return False

	return True


if __name__ == '__main__':
	main()