def reverse(s):
	l=s.split()
	l=l[::-1]
	for word in l:
		print(word,end=" ")
	print('\n')
	l=l[::-1]
	for i in range(len(l)):
		l[i] = l[i][::-1]
	for word in l:
		print(word, end=" ")
st = input('enter a string')
reverse(st)