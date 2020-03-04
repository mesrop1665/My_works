m  = 'ptyrty'
r = 0

def summa(g):
    if type(g) != int:
        print(TypeError)

    else:
        for i in range(len(str(g))):
            r += int(str(m)[i])
            print(r)

summa(m)