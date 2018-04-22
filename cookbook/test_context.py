class MyContext(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __enter__(self):
        print('you are entering the context!')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('You are exiting')

    def introduce(self):
        print(self.a, self.b)


if __name__ == '__main__':
    with MyContext(1, 5) as con:
        con.introduce()
