def add(a):
	sum = 0
	for i in range(0,len(a)):
		sum+=a[i]
	return sum
l=list(map(int , input('enter the numbers ').split()))
print(add(l))
