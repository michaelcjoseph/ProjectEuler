#Project Euler 28
#Number spiral diagnols

# 3x3 - 2nd ring
# 5x5 - 3rd ring
# 7x7 - 4th ring
# 9x9 - 5th ring
# ...

# 43 44 45 46 47 48 49
# 42 21 22 23 24 25 26
# 41 20  7  8  9 10 27
# 40 19  6  1  2 11 28
# 39 18  5  4  3 12 29
# 38 17 16 15 14 13 30
# 37 36 35 34 33 32 31

# 1, 9 (3x3), 25 (5x5), 49 (7x7) ... = a^2 (a x a)
# 1, 5 (3x3), 17 (5x5), 37 (7x7) ... = a^2 - 4*((a-1)/2) (a x a)
# 1, 7 (3x3), 21 (5x5), 43 (7x7) ... = a^2 - (a-1) (a x a)
# 1, 3 (3x3), 13 (5x5), 31 (7x7) ... = (a^2 - (a-1)) - 4*((a-1)/2) (a x a)

import math

diag_sum = 1

for x in range(3, 1002, 2):
	diag_sum += pow(x, 2)
	diag_sum += pow(x, 2) - 4*((x-1) / 2)
	diag_sum += pow(x, 2) - (x - 1)
	diag_sum += pow(x, 2) - (x - 1) - 4*((x-1) / 2)

print diag_sum