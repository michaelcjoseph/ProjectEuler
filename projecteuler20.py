#Project Euler 20
#Factorial digit sum

import math

num = math.factorial(100)
num_string = str(num)

sum = 0

for i in num_string:
	sum += int(i)

print sum