import json


class Parent(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


class Child(object):
    def __init__(self, p, test):
        self.p = p
        self.test = test
        self.db = None

    def get_ready_flag(self):
        self.is_ready = True
        print self.is_ready
    # @property
    # def db(self):
    #     self.db = json.load(open('wh.json'))
    #
    # @db.gette
    # def show_detail(self):
    #     self.p.show_info()
    #     print(self.test, self.db)

    def generate_db(self):
        db = {'dbtype': "Spark", 'servername': 'aws-231.com'}
        json.dump(open('wh.json', 'w'), db)


p = Parent('AA', 32)
p.show_info()
c = Child(p, 'Hahaha')
c.get_ready_flag()
