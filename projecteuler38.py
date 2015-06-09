# Project Euler 38
# Pandigital Multiples

import math

def main():
	num = 1

	for i in range(1, 10000, 1):
		x = ConcatProducts(i)
		if x >= num:
			if IsPandigital(x):
				num = x

	print num


def ConcatProducts(n):
	concat = str(n)
	count = 2

	while len(concat) < 9 and count < 10:
		concat += str(n*count)
		count += 1

	return concat


def IsPandigital(n):
	if len(str(n)) == 9:
		n_digits = []
		for i in range(0, len(str(n)), 1):
			n_digits.append(int(str(n)[i]))

		if 1 in n_digits:
			if 2 in n_digits:
				if 3 in n_digits:
					if 4 in n_digits:
						if 5 in n_digits:
							if 6 in n_digits:
								if 7 in n_digits:
									if 8 in n_digits:
										if 9 in n_digits:
											return True

	return False


if __name__ == '__main__':
	main()