#Project Euler 25
#1000-digit Fibonacci Number

fib = [1, 1]

while len(str(fib[-1])) < 1000:
	fib.append(fib[-1] + fib[-2])

print fib[-1]
print len(fib)