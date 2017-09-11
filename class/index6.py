class student():

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_ns(self):
        print(self.name, self.score)


s1 = student('tom', 95)
s1.print_ns()


#继承
class Animal():

    def run(self):
        print("Animal is runing")


class Dog(Animal):
    pass


class bird(Animal):

    def run(self):
        print("bird is runing")


class toy():

    def run(self):
        print("toy is running")


def run_twice(Animal):
    Animal.run()


d = Dog()
d.run()
run_twice(Dog())
run_twice(bird())
run_twice(toy())

#静态语言 vs 动态语言

#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了