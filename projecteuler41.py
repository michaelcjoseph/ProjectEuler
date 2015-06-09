# Project Euler 41
# Pandigital Prime

import math

def main():
	prime = 1

	for i in range(98764321, 1, -1):
		if IsNPandigital(i):
			if IsPrime(i):
				prime = i
				break

	print prime

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

def IsNPandigital(n):
	if len(str(n)) <= 9:
		for i in range(1, len(n_digits) + 1, 1):
			if str(i) not in str(n):
				return False

	return True


if __name__ == '__main__':
	main()