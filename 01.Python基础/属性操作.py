class A(object):

    @property
    def age(self):
        return self._age + 10

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    a = A()
    a.age = 10
    print a.age