# class Shape:
#     def calculate_area(self):
#         return None
#
# class Square(Shape):
#     side_length = 2
#     def calculate_area(self):
#         return self.side_length * 2
#
# class Triangle(Shape):
#     base_length = 4
#     height = 3
#     def calculate_area(self):
#         return 0.5 * self.base_length * self.height
#
#
# class Rectangle(Shape):
#     def calculate_area(self):
#         return "rectangle area"
#
#
# shapes = [Triangle(), Square(), Triangle(), Rectangle()]
#
# for shape in shapes:
#     print(shape.calculate_area())


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError
        self.__name = value


p = Person("Test")
p.name = "Test 2"
