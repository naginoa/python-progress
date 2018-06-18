for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()

print()

for i in range(1, 10):
    str = '        '
    for j in range(i, 10):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()
    print( i * str, end='')