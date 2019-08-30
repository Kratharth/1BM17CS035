num = int(input('enter the number'))
lis1 = []
for i in range(1,int(num/2)+1):
	if num % i == 0:
		lis1.append(i)
lis1.append(num)
print('the list of divisors are : ',end=" ")
print(lis1)
