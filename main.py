class Example:
    pi = 3.14

    def __init__(self, text):
        self.text = text
        self.a = 7

    def print_text(self):
        return 'SoftUni'


text_name = input()
x = Example(text_name)
y = Example("test 2")
x.new_attr = "asd"
print(x.text)
print(y.pi)


x.pi = 5
print(x.pi)
print(y.pi)
print(Example.pi)

Example.new_something = 8
print(x.new_something)