l = []
m = True
f = [11,2,3,12]
for i in f:
    for g in range(2,i):
        if i%g == 0:
            m= False
    if m:
        l.append(i)
print(l)