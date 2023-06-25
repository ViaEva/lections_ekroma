class SomeClass:
    def __init__(self):
        self.__param = 42

    def p(self):
        return self.__param
obj = SomeClass()
print(obj.p())
