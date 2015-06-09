# Project Euler 33
# Digit Canceling Fractions

import fractions

def main():

	num = 1
	den = 1
	counter = 0

	for a in range(10,100,1):
		for b in range(10,100,1):
			decimal = float(a) / float(b)
			digit_decimal = 0.0
			
			if decimal < 1:
				if ((a % 10 == 0) & (b % 10 == 0) | (a == b)):
					digit_decimal = 0.0
				else:
					a_digits = [int(str(a)[0]), int(str(a)[1])]
					b_digits = [int(str(b)[0]), int(str(b)[1])]

					if (a_digits[0] in b_digits) & (b_digits[1] != 0):
						if a_digits[0] == b_digits[0]:
							digit_decimal = float(a_digits[1]) / float(b_digits[1])
						else:
							digit_decimal = float(a_digits[1]) / float(b_digits[0])

					elif (a_digits[1] in b_digits) & (b_digits[1] != 0):
						if a_digits[1] == b_digits[0]:
							digit_decimal = float(a_digits[0]) / float(b_digits[1])
						else:
							digit_decimal = float(a_digits[0]) / float(b_digits[0])

				if decimal == digit_decimal:
					counter += 1
					print "%d / %d" %(a,b)
					num *= a
					den *= b

	divisor = fractions.gcd(num, den)
	solution = den / divisor

	print counter
	print num
	print den
	print divisor
	print solution


if __name__ == '__main__':
	main()