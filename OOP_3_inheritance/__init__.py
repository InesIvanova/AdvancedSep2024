class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return "Hi, I am " + self.get_full_name()


class Student(Person):
    def __init__(self, first_name, last_name, fac_number):
        super().__init__(first_name, last_name)
        self.fac_number = fac_number

    def get_fac_number(self):
        return self.fac_number

    def get_info(self):
        result = super().get_info()
        result += f"\n I am a student with fac. number {self.fac_number}"
        return result





p = Person("Test", "Testov")
print(p.first_name)
print(p.last_name)
print(p.get_full_name())

s = Student("Ines", "Ivanova", "036MD")
print(s.first_name)
print(s.last_name)
print(s.fac_number)
print(s.get_full_name())
print(s.get_fac_number())
print(s.get_info())
