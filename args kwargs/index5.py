#*args  和  **kwargs 指可变参数       前者是value 后者是 键值对
def f(a, *args):
    print(a)
    for b in args:
        print(b)


def fun_var_kwargs(farg, **kwargs):
    print
    "arg:", farg
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))



#f(1)
#f(1,2,3,4,5,6,7)

fun_var_kwargs(farg=1, a = 1, b = 2)