#Brian Sampson
#I pledge my honor that I have abided by the Stevens Honor System
#CS306

from timeit import default_timer as timer
#Naive method
def SlowExpMod(a, b, n):
    r = 1
    for i in range(b):
        r = r * a % n
    return r

#Efficient modular exponentiation using precomputation
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

start = timer()
print("Result from fast mod: " + str(fastExpMod(2**31, 2**32 - 1, 100003)))
end = timer()

print("Fast Method Time = " + str(end - start))

start = timer()
print("Result from slow mod: " + str(SlowExpMod(2, 2**24 -  1, 100003)))
end = timer()

print("Slow Method Time = " + str(end - start))

print(SlowExpMod(2**31, 2**32 - 1, 100003))