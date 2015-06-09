# Project Euler 37
# Trunctable primes

import math

def main():
	sums = 0
	count = 0

	for i in range(10, 1000000, 1):
		check = 0
		trunc_list = TruncList(i)

		for j in trunc_list:
			if IsPrime(j):
				check += 1

		if check == len(trunc_list):
			print trunc_list
			sums += i
			count += 1

	print sums
	print count


def TruncList(n):
	n_digits = []
	n_trunc = [n]

	for i in range(0, len(str(n)), 1):
		n_digits.append(str(n)[i])

	for i in range(0, len(n_digits), 1):
		trunc1 = ""
		trunc2 = ""

		for j in range(i, len(n_digits), 1):
			trunc1 += n_digits[j]

		if int(trunc1) not in n_trunc:
			n_trunc.append(int(trunc1))

		for j in range(0, i+1, 1):
			trunc2 += n_digits[j]

		if int(trunc2) not in n_trunc:
			n_trunc.append(int(trunc2))

	return n_trunc


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