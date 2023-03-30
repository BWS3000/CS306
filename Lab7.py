import random
import math

def isPrime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if(n % i == 0):
            return False
    return True

def getSGPrimes():
    rand = random.randint(2 ** 31, 2 ** 32 - 1)
    while(not isPrime(rand) or not isPrime(rand * 2 + 1)):
        rand = random.randint(2 ** 31, 2 ** 32 - 1)
    return (rand, rand * 2 + 1)

def getRandomKeys():
    return (random.randint(1, Q), random.randint(1, Q))

Q, P = getSGPrimes()

a, b = getRandomKeys()

def fastExpMod(a, b, n) :
    if (b == 0) :
        #when b = 0
        return 1
    elif(b % 2 == 0) :
        #b is even
        tmp = fastExpMod(a, b / 2, n)
        return (tmp * tmp) % n
    else :
        #b is odd
        tmp = fastExpMod(a, b - 1, n)
        return (a * tmp) % n

def g():
    g = 2
    while(fastExpMod(g, Q, P) != 1):
        g += 1
    return g

def publicKeys():
    gVal = g()
    x = fastExpMod(gVal, a, P)
    y = fastExpMod(gVal, b, P)
    return (x, y)

def sharedSecret(publicKeys):
    return (fastExpMod(publicKeys[0], b, P), fastExpMod(publicKeys[1], a, P))

print("Q prime value: " + str(Q))
print("P prime value: "  + str(P))
print("Secret key a = " + str(a))
print("Secret key b = " + str(b))
print("g = " + str(g()))
pKeys = publicKeys()
print("X Value : g^a mod P = "  + str(pKeys[0]))
print("Y Value : g^b mod P = "  + str(pKeys[1]))
sharSecret = sharedSecret(pKeys)
print("Shared Secret 1 : x^b mod P : " + str(sharSecret[0]))
print("Shared Secret 2 : y^a mod P : " + str(sharSecret[1]))
print("Are the shared secrets equal? " + str(sharSecret[0] == sharSecret[1]))