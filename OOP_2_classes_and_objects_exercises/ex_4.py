from typing import Optional


class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(
        self, ingredient: str, quantity: int, price_per_quantity: float
    ) -> Optional[str]:
        if self.ordered:
            return self.get_pizza_already_ordered_message()
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(
        self, ingredient: str, quantity: int, price_per_quantity: float
    ) -> Optional[str]:
        if self.ordered:
            return self.get_pizza_already_ordered_message()

        if ingredient not in self.ingredients:
            return (
                f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            )

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        if self.ordered:
            return self.get_pizza_already_ordered_message()

        self.ordered = True
        formatted_ingredients = [
            f"{ingredient}: {quantity}"
            for ingredient, quantity in self.ingredients.items()
        ]
        return (
            f"You've ordered pizza {self.name} "
            f"prepared with {', '.join(formatted_ingredients)} "
            f"and the price will be {self.price}lv."
        )

    def get_pizza_already_ordered_message(self) -> str:
        return f"Pizza {self.name} already prepared, and we can't make any changes!"