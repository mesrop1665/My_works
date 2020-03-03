m  = 122
r = 0
if type(m) != int:
    print(type(m))

else:
    for i in range(len(str(m))):
        r += int(str(m)[i])
    print(r)