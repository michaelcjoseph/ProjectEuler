#Project Euler - Problem 16
#Power Digit Sum - What is the sum of the digits of the number 2^1000

#Calculate the actual number
num = pow(2,1000)

#Convert it into a string to easily iterate through
num_str = str(num)

#Initialize sum variable
digit_sum = 0

#For loop that calculates sum
for x in num_str:
	digit_sum += int(x)

print digit_sum