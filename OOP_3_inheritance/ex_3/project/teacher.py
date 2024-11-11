from project.employee import Employee
from project.person import Person


class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."