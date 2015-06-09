# Project Euler 32
# Pandigital Products

import math

def main():
	sums = 0
	products = []

	for a in range(1,9999,1):
		limit = 9999 / a
		for b in range(1,limit,1):
			c = a * b

			if c not in products:
				string = str(a) + str(b) + str(c)

				if len(string) == 9:
					string_list = []
					for i in range(0,9,1):
						string_list.append(int(string[i]))

					if 1 in string_list:
						if 2 in string_list:
							if 3 in string_list:
								if 4 in string_list:
									if 5 in string_list:
										if 6 in string_list:
											if 7 in string_list:
												if 8 in string_list:
													if 9 in string_list:
														sums += c
														products.append(c)


	print sums


if __name__ == '__main__':
	main()