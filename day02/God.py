class Human(object):
    def __init__(self, name):
        self.__name = name

    def walk(self):
        print (self.name + " is walking")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    pass


class Man(Human):
    def __init__(self, name, has_wife):
        super(Man, self).__init__(name)
        self.__has_wife = has_wife

    def smoke(self):
        print ("A man maybe smoke")

    def drink(self):
        print ("A man maybe drink")
    pass


class Woman(Human):
    def __init__(self, name, has_husband):
        super(Woman, self).__init__(name)
        self.__has_husband = has_husband

    def shopping(self):
        print ("A woman always go shopping")

    def make_up(self):
        print ("A woman always make up")
    pass
