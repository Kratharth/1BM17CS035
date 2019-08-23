def check(li,a):
	return a in li
li = list(map(int, input('enter the numbers').split()))
b= int(input('enter the number to search'))
print(check(li,b))
