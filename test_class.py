class Person():
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('getter method')
        return self._name

    def set_name(self, name):
        print('setter method')
        self._name = name
    name = property(get_name, set_name)


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self._email = email

    @property
    def email(self):
        print('call getter')
        return self._email

    @email.setter
    def email(self, email):
        print('call setter')
        self._email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
bob.email = 'dhong@126.com'
print(bob.email)
# bob.name = 'Bob Wayne'
# print(bob.name)
# bob.set_name('Bob YY')
# print(bob.get_name())
