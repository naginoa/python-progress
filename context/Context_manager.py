from contextlib import contextmanager


#普通版
def m1():
    f = open("output.txt", "w")
    f.write("python之禅")
    f.close()
#如果在调用 write 的过程中，出现了异常进而导致后续代码无法继续执行，close 方法无法被正常调用，因此资源就会一直被该程序占用而无法被释放。


#进阶版
def m2():
    f = open("output.txt", "w")
    try:
        f.write("python之禅")
    except IOError:
        print("oops error")
    finally:
        f.close()


#高级版
def m3():
    with open("output.txt", "w") as f:
        f.write("Python之禅")
#当离开 with 代码块的时候，系统会自动调用 f.close() 方法


#自己定义上下文管理器
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()


with File('out.txt', 'w') as f:
    print("writing")
    f.write('hello, python')


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()
#yield 之前的语句在 __enter__ 方法中执行，yield 之后的语句在 __exit__ 方法中执行。紧跟在 yield 后面的值是函数的返回值。


with my_open('out.txt', 'w') as f:
    f.write("hello , the simplest context manager")