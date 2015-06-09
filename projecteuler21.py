#Project Euler 21
#Amicable Numbers

import math

#This function returns the sum of the divisors of the argument
def divisor_sum(num):
	sums = 1

	for i in range(2, int(math.sqrt(num)) + 1, 1):
		if num % i == 0:
			sums += i + (num / i)

	return sums

def main():
	amicable_sums = 0
	amicable_numbers = []

	for x in range(1, 10000, 1):
		if x not in amicable_numbers:
			y = divisor_sum(x)
			if x == divisor_sum(y) and x != y:
				amicable_sums += x + y
				amicable_numbers.append(x)
				amicable_numbers.append(y)

	print amicable_sums
	print amicable_numbers

if __name__ == '__main__':
  main()