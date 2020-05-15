class SingleTon(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class ConcreteClass(SingleTon):
    pass


if __name__ == '__main__':
    instance_c = ConcreteClass()
    instance_a = SingleTon()
    instance_b = SingleTon()
    instance_d = ConcreteClass()
    print(instance_a is instance_b)
    print(instance_a is instance_c)
    print(instance_d is instance_c)
    print(instance_d is instance_a)
