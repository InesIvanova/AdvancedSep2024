from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        return "eating"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "meow"




animals = [Dog(), Cat()]

for a in animals:
    print(a.sound())
    print(a.eat())


a = Animal()