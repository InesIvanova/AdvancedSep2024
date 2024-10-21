def sum_nums(a, b):
    return a + b


print(sum_nums(5, 6))
print(sum_nums)
class Phone:
    def __init__(self, color, size, pixels=1060):
        self.color = color
        self.size = size
        self.camera = pixels
        self.is_turn_on = False

    def turn_on(self):
        self.is_turn_on = True

    def make_a_call(self):
        if not self.is_turn_on:
            raise Exception("Can not maake calls while switched off")
        return "making a call"



class Iphone(Phone):
    def __init__(self, color, size, pixels=1060):
        super().__init__(color, size, pixels=1060)
        self.imessage = True


phone1 = Phone("black", 10)
phone2 = Phone("green", 5, 2000)
phone3 = Phone("yellow", 5)
phone4 = Phone("black", 5)
phone5 = Phone("black", 10)

print(phone1.color)

phone1.color = "red"

phone1.turn_on()
print(phone1.make_a_call())

a = [1, 2, 3]
a.append(5)

