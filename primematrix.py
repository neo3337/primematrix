"""
primematrix.py
By Neo.
The problem of evil.
Maya.

Artificial intelligence by Arsene Denisov.

GNU GPL license
"""

import math
import itertools

primeList = []
primeMatrix = []
numberOfPrimes = 4



def generatePrime(n):
    X = 0
    i = 2
    flag = False
    while(X < n):
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if (i%j == 0):
                flag = False
                break
        if(flag):
            primeList.append(i)
            X+=1
        i+=1

generatePrime(numberOfPrimes)

primeMatrix = list(itertools.permutations(primeList))

print(primeMatrix)
