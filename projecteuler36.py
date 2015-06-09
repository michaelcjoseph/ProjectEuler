# Project Euler 36
# Double Base Palindromes

import math

def main():
	sums = 0

	for i in range(1, 1000000, 1):
		if IsPalindrome(i) and IsPalindrome(ToBinary(i)):
			sums += i

	print sums


def IsPalindrome(n):
	n_string = str(n)
	n_digits = []

	for i in range(0, len(n_string), 1):
		n_digits.append(n_string[i])

	end = len(n_digits) - 1
	for i in range(0, (len(n_digits)/2 + 1), 1):
		if n_digits[i] != n_digits[end - i]:
			return False

	return True


def ToBinary(n):
	return int("{0:b}".format(n))


if __name__ == '__main__':
	main()