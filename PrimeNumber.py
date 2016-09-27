"""
Calculate all the price number, and k-th prime number withing 1~n

Source: http://python.jobbole.com/86496/
"""

def allPrimeNumber(n):
    # Initiate an array representing whether the number is prime:
    # 1 means yes and 0 means no
    numArray = [1] * (n+1)
    # 1 not defined
    numArray[1] = 0

    for i in xrange(2, n/2):
        j = i * 2
        while j <= n:
            # mark j as not a Prime number
            numArray[j] = 0
            j += i
    print(numArray)
    return numArray

def prime(n, x):
    # return the n-th prime number in x
    # i is the cursor
    i = 1
    # j records the total number of
    j = 1
    while j <= n:
        if x[i] == 1:
            j += 1
        i += 1
    return i - 1



def printPrimeNumber(x):
    for k in xrange(2, len(x)):
        if x[k] == 1:
            print k

if __name__ == '__main__':
    n = 10
    primelist = allPrimeNumber(n)
    printPrimeNumber(primelist)
    print(prime(4, primelist))

