#Project Euler 23
#Non-abundant sums

import math

#This function returns the sum of the divisors of the argument
def divisor_sum(num):
	sums = 1

	for i in range(2, int(math.sqrt(num)) + 1, 1):
		if num % i == 0:
			sums += i + (num / i)

	return sums

def main():
	sums = 0 #final solution variable

	#First create a list of all abundant numbers up to 28,123
	abundant_nums = []
	for x in range(12, 28123, 1):
		if divisor_sum(x) > x:
			abundant_nums.append(x)

	#Second iterate down from the analytical max (28123)
	#Subtract every number in the abundant_nums list from the current value of the for loop
	#If a dividend returned also exists in the abundant_nums list, then we know the value is
	#abundant sum, and will not be appended to the new list
	non_abundant_sums = []
	for x in range(1, 28123, 1):
		if x < 24:
			non_abundant_sums.append(x)
		else:
			counter = 0
			for i in abundant_nums:
				if abs(x - i) in abundant_nums:
					counter += 1
			if counter == 0:
				non_abundant_sums.append(x)

	#Calculate sum of non_abundant_sums
	for x in non_abundant_sums:
		sums += x

	print sums

if __name__ == '__main__':
  main()