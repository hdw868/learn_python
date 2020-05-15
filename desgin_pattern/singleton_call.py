class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConcreteClass(metaclass=Singleton):
    pass


class SubConcreteClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    instance_c = SubConcreteClass()
    instance_a = ConcreteClass()
    instance_b = ConcreteClass()
    instance_d = SubConcreteClass()
    print(instance_a is instance_b)
    print(instance_a is instance_c)
    print(instance_d is instance_c)
    print(instance_d is instance_a)
