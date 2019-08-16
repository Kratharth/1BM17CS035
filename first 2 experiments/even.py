list1= list(map(int,input('enter the numbers').split()))
list2 =[]
for ele in list1:
	if( ele %2 == 0):
		list2.append(ele)
print(list2)
