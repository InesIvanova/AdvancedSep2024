class Animal:
    def eat(self):
        return "eat"


class Cat(Animal):
    def breathe(self):
        pass


class Dog(Animal):
    def eat(self):
        result = super().eat()
        return "Dog " + result

    def say_hi(self):
        Animal.eat(self)


d = Dog()
print(d.hi())