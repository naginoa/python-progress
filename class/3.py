import math

def isPrime(m):
#m = int(input("input:"))
    k = int(math.sqrt(m))
    for i in range(2, k+2):
        if m % i == 0:
            break
    if i == k+1:
        print("sushu")
    #else:
        print("heshu")


isPrime(3)
isPrime(4)