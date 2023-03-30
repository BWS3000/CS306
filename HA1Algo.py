from cmath import log
import math

for x in range(1, 11):
    print("First algorith: " + str(4 * x ** 3) + ", Second algorithm: " + str(64 * x * math.log(x, 2)))