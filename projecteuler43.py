# Project Euler 43
# Sub-string divisibility

def main():
	primes = [2, 3, 5, 7, 11, 13, 17]
	sums = 0

	for i in range(1000000000, 9876543201, 1):
		if IsPandigital(i):
			divisible = True
			for j in range(1, 8, 1):
				if int(str(i)[j] + str(i)[j+1] + str(i)[j+2]) % primes[j-1] != 0:
					divisible = False
					break

			if divisible:
				sums += i

	print sums


def IsPandigital(n):
	if len(str(n)) == 10:
		if '1' in str(n):
			if '2' in str(n):
				if '3' in str(n):
					if '4' in str(n):
						if '5' in str(n):
							if '6' in str(n):
								if '7' in str(n):
									if '8' in str(n):
										if '9' in str(n):
											if '0' in str(n):
												return True

	return False

if __name__ == '__main__':
	main()