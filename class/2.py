import math


#m = int(input("input:"))
flag = 0
for m in range(100, 1001):
    k = int(math.sqrt(m))
    for i in range(2, k+2):
        if m % i == 0:
            break
    if i == k+1:
        flag += 1
        print(m, "", end='')
        if flag % 5 == 0:
            print()
    #else:
        #print(m, "heshu")