'''

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
def isPrime(x):
    #x>2
    result = True
    for i in range(3,int(x**0.5)+1):
        if x % i == 0:
            result = False
            break
    return result

def GoldbachOtherConjecture():
    i = 23
    
    while True:
        count = 0
        if not isPrime(i):
            for j in range(3, i, 2):
                if isPrime(j) and (int(((i - j)/2)**0.5) - ((i-j)/2)**0.5) == 0:
                    count += 1
        else:
            count += 1
        if count == 0:
            break
        i += 2
    return i



final = GoldbachOtherConjecture()
print(final)
        