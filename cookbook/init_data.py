class Structure(object):
    _fields = []

    def __init__(self, *args):
        if len(args) < len(self._fields):
            raise TypeError('incorrect length of args')

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

    def __str__(self):
        for field in self._fields:
            print(filed)


if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

        def show(self):
            print(self.name, self.shares, self.price)

    class Point(Structure):
        _fields = ['x', 'y']

        def show(self):
            print(self.x, self.y)

    stock = Stock('myname', 0.1, 30)
    point = Point(5, 3)
    stock.show()
    point.show()
