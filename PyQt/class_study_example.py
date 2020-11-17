class Circle(object):
    pi = 3.14159265
    def __init__(self,r):
        self.r = r
    def get_area(self):
        return self.r**2 * self.pi

circle00 = Circle(1)
circle01 = Circle(3)
print(circle00.get_area())
print(circle01.get_area())

# print(circle00.r)
# print(circle01.r)
# print(circle00.pi)
# print(circle01.pi)

# Circle.pi = 3.14

# print(circle00.pi)
# print(circle01.pi)

# circle00.pi = 3.153654624525423
# print(circle00.pi)
# del circle00.pi
# print(circle00.pi)

# del Circle.pi
# print(circle00.pi)



