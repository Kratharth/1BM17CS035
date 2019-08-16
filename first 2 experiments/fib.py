def fib(b):
	if(b == 1):
		return 0
	elif( b == 2):
		return 1
	else:
		return fib(b-1)+fib(b-2)
a = int(input('enter the number of fibonache series'))
for i in range(1,a+1):
	print(fib(i))

