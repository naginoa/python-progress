def yf():
    yield from range(1, 5)
    yield from range(10, 15)


#可以翻译为:
def yf():
    for x in range(1, 5):
        yield x
    for x in range(10, 15):
        yield x


#关键是这玩意还可以“递归”：
def yf2():
    yield from yf()
    # 效果等同：
    # for x in yf():
    #     yield x


for x in yf():
        print(x)

for x in yf2():
    print(x)

#所以yield from是一个“代理”