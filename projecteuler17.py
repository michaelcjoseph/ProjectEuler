#Project Euler 17
#Number Letter Counts

#Set up dictionary that equates numbers in their numerical form
#to numbers in their word form
nums = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen',
	20: 'twenty',
	30: 'thirty',
	40: 'forty',
	50: 'fifty',
	60: 'sixty',
	70: 'seventy',
	80: 'eighty',
	90: 'ninety',
	100: 'hundred',
	1000: 'thousand'
}

#Initialize letter_count variable
letter_count = 0

#For loop that will iterate through all numbers
for x in range(1, 1001, 1):
	#first 19 numbers:
	if x >= 1 and x <= 19:
		letter_count += len(nums[x])

	#numbers 20 through 99
	elif x >= 20 and x <= 99:
		string = str(x)
		tens = int(string[0]) * 10 #calculate tens digit of number
		ones = int(string[1]) #calculate ones digit of number
		letter_count += len(nums[tens]) + len(nums[ones])

	#numbers 100 through 999
	elif x >= 100 and x <= 999:
		string = str(x)
		hundreds = int(string[0])
		tens = int(string[1]) * 10
		ones = int(string[2])

		if tens == 0 and ones == 0:
			letter_count += len(nums[hundreds]) + len(nums[100])
		else:
			letter_count += len(nums[hundreds]) + len(nums[100]) + len('and')
			if (tens+ones) >= 1 and (tens+ones) <= 19:
				letter_count += len(nums[(tens+ones)])
			else:
				letter_count += len(nums[tens]) + len(nums[ones])
	#number 1000
	elif x == 1000:
		letter_count += len(nums[x]) + len(nums[1])
	else:
		print 'break'

print letter_count
			