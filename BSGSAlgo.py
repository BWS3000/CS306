#Brian Sampson
#CS306
#I pledge my honor that I have abided by the Stevens Honor System

from cmath import sqrt


from logging import exception


def isPrimeNumber(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def validParameters(integer, mod):
    if(integer > 0 and mod > 0 and mod > integer and isPrimeNumber(mod)):
        return True
    else:
        return False

def getInverseMod(integer, mod):
    #if(not validParameters(integer, mod)):
        #raise Exception("a and b must be > 0. b must be > a. a must be")

    modVal = mod
    def extended_gcd(integer, mod):
        if integer == 0:
            return (mod, 0, 1)
        else:
            gcd, x, y = extended_gcd(mod % integer, integer)
            return (gcd, y - (mod // integer) * x, x)
    tup = extended_gcd(integer, mod)
    return (modVal + tup[1]) % modVal



def BSGSAlgo(g, p, b):
    #First step is to find m
    #int m = sqrt(p) + 1
    arrj = []
    arri = []

    m = int(sqrt(p).real + 1)

    for index in range(0, m):
        arrj.append(g ** index)

    for index in range(0, m):
        if(m * index == 0):
            arri.append(b * 1)
        else:
            arri.append((b * getInverseMod(g ** (index * m), p)) % p)

    for i in arri:
        for j in arrj:
            if (i == j):
                iVal = arri.index(i)
                jVal = arrj.index(j)
                break
    return m * iVal + jVal


#Test cases that where given in class
#BSGSAlgo(g, p, b)
print(BSGSAlgo(2,37,3))


