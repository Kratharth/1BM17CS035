def printboard(num):
	for i in range(num):
		print(' ---' * num)
		print('|  ' * (num+1))
	print(' ---' * num)
num = int(input('enter the number of rows'))
printboard(num)	
