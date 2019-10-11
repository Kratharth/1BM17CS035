with open('prime.txt') as p :
	prime = list(map(int, p.read().split(', ')))
with open('happy.txt') as h :
	happy = list(map(int , h.read().split(', ')))
prime = set(prime)
happy = set(happy)
print(' '.join(map(str,prime.intersection(happy))))
