sum = 0
for i in range(0,1001):
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        sum += 1

print(sum)