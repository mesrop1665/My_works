def getCount(s):
    num_vowels = 0
    f = ['a','i','o','e']
    for i in s:
        if i in f:
            num_vowels += 1
    
    print(num_vowels)

getCount('python')