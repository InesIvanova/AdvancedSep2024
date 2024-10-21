class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

    def __repr__(self):
        return f"{self.model} {self.engine}"

car = Car("Kia", "Rio", "1.3L B3 I4")
# car2 = Car("Toyota", "Corolla", "1.8L")
# cars = []
#
# n = int(input())
# for _ in range(n):
#     name, model, engine = input().split()
#     car = Car(name, model, engine)
#     cars.append(car)

print(car)
