class Person(object):
    def __new__(cls, *args, **kargs):
        print('__new__ called')
        return super(Person, cls).__new__(cls, *args, **kargs)

    def __init__(self, name, age):
        print('__init__ called')
        self.name = name
        self.age = age

    def __call__(self):
        print(self.name, self.age)


p1 = Person('Wayne', 30)
p2 = Person('Amanda', 30)
p1()
p2()
