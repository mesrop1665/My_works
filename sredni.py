a = 'pytyer'
l = []
for i in a:
	l.append(i)

if len(l)%2 == 0:
	f = int(len(l)/2)-1
	m = f + 1
	print(f'{l[f]}{l[m]}')

if len(l)%2 != 0:
	f = int(len(l)/2)
	print(l[f])