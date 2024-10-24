class Point:
    some = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    # def __str__(self):
    #     return f"The point has coordinates ({self.x},{self.y})"

    def __repr__(self):
        return "asd"


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
p_as_dict = p.__dict__
print(type(p))
print(id(p))
print(type(p_as_dict))
print(id(p_as_dict))
