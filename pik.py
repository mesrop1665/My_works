def friend(x):
    l = []
    for i in x:
        if len(i) == 4:
            l.append(i)
    print(l)

friend(["Ryan", "Kieran", "Mark"])