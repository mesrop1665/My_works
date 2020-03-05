def square_digits(num):
    r = ""
    for i in range(len(str(num))):
        i = str(num)[i]
        r += str(int(i)*int(i))
    
    return int(r)

square_digits(1222)