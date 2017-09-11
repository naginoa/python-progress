import time


f = lambda x:x * x
print(5)

a = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a)

#装饰器
def log(func):
    def wrapper(*args, **kw):
        print("call %s :" % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print(time.asctime(time.localtime(time.time())))


now()
f = now
f()
print(f.__name__)
#结果都是wrapper
print(now.__name__)