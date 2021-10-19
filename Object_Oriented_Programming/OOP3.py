# Object-Oriented Programming

class Robot:
    def __init__(self, name=None, year=None):
        self.name = name
        self.year = year

    def greetings(self):
        return "Welcome! My master calls me {}".format(self.name)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_year(self):
        return self.year

    def set_year(self, dates):
        self.year = dates


x = Robot()
x.set_name("droid1")
print(x.greetings())
y = Robot()
y.set_name(x.get_name())
print(y.get_name())

# x.name = "droid1"
# print(x.name)

