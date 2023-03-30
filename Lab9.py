#Brian Sampson
#I pledge my honor that I have abided by the Stevens Honor System

import random
import math
import hashlib

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

def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return x

#Get random e value such that 1 < e < Phi(N) and gcd(e, Phi(N)) == 1
#Brute force find random e
def finde():
    e = 0
    while(not (1 < e and e < phiN and computeGCD(e, phiN) == 1)):
        e = random.randint(1, phiN)
    return e

#e*d = 1(mod Phi(N))
def getInverseMod(integer, mod):
    modVal = mod
    def extended_gcd(integer, mod):
        if integer == 0:
            return (mod, 0, 1)
        else:
            gcd, x, y = extended_gcd(mod % integer, integer)
            return (gcd, y - (mod // integer) * x, x)
    tup = extended_gcd(integer, mod)
    return (modVal + tup[1]) % modVal

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

#RSA Key generation
Q, P = getSGPrimes()

N = P * Q

phiN = (P - 1) * (Q - 1)

e = finde()

d = getInverseMod(e, phiN)

#Digital Signature by sender
M = "important message"
digest = int(hashlib.sha256(M.encode('utf-8')).hexdigest(), 16)
digest60 = bin(digest)[0:61]
DS = pow(int(digest60, 2), d, N)

#Sending M and DS to reciever
digestPrime = int(hashlib.sha256(M.encode('utf-8')).hexdigest(), 16)
digestPrime60 = bin(digest)[0:61]

result = pow(DS, e, N)

print("Value of Q : ", Q)
print("Value of P : ", P)
print("Value of N : ", N)
print("Value of PhiN : ", phiN)
print("Value of e : ", e)
print("Value of d : ", d)
print("Value of DS : ", DS)
print("Is the message signed by the sender? ", bin(result) == digestPrime60)



