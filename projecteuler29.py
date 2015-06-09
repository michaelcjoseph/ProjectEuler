# Project Euler 29
# Distinct Powers

import math

def main():
	sequence = []

	for a in range(2,101,1):
		for b in range(2,101,1):
			c = math.pow(a,b)

			if c not in sequence:
				sequence.append(c)

	print len(sequence)

if __name__ == '__main__':
	main()