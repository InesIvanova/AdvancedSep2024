class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])



custom_pizza = Pizza(["tomato sauce", "parmesan", "apple", "parmigiano"])


pizza = Pizza.quattro_formaggi()