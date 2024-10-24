class Dog:
    tricks = []     # mistaken use of a class variable
    a = 5

    def __init__(self, name):
        self.name = name


poodle = Dog("Bella")
beagle = Dog("Max")
poodle.tricks.append('roll over')
print(beagle.tricks)
print(poodle.a)
print(beagle.a)
poodle.a = 10
print(poodle.a)
print(beagle.a)