# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume


class Cuboid:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSurface(self):
        return (self.a * self.b + self.b * self.c + self.c * self.a) * 2

    def getVolume(self):
        return self.a * self.b * self.c


myCuboid_1 = Cuboid(1, 1, 1)
print(myCuboid_1.getSurface())
print(myCuboid_1.getVolume())

myCuboid_2 = Cuboid(1, 2, 3)
print(myCuboid_2.getSurface())
print(myCuboid_2.getVolume())


