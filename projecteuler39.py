# Project Euler 39
# Integer Right Triangles

# right triangle - a^2 + b^2 = c^2
# p = a + b + c
# Maximize the number of {a,b,c} combinations for any given p, p <= 1000

import math

def main():
	rt_combos = []
	rt_perim = {}

	for a in range (3, 1000, 1):
		for b in range (4, 1000, 1):
			c = math.sqrt(math.pow(a,2) + math.pow(b, 2))
			if c.is_integer():
				if ([a,b,c] not in rt_combos) and ([b,a,c] not in rt_combos):
					p = a + b + c
					if p <= 1000:
						if p in rt_perim:
							rt_perim[p] += 1
						else:
							rt_perim[p] = 1

						rt_combos.append([a,b,c])

	perim = 0
	total_combos = 0

	for key in rt_perim:
		if rt_perim[key] > total_combos:
			perim = key
			total_combos = rt_perim[key]

	print total_combos
	print perim


if __name__ == '__main__':
	main()