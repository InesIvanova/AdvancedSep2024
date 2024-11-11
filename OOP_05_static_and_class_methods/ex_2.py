class Shop:
    def __init__(self, name: str, type: str, capacity: int) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items: dict[str, int] = {}

    @classmethod
    def small_shop(cls, name: str, type: str) -> "Shop":
        return cls(name, type, 10)

    def add_item(self, item_name: str) -> str:
        if self.capacity <= sum(self.items.values()):
            return "Not enough capacity in the shop"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"

        if self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


import unittest

class ShopTests(unittest.TestCase):
    def setUp(self):
        self.fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)

    def test_add_item_success(self):
        result = self.fresh_shop.add_item("Bananas")
        self.assertEqual(self.fresh_shop.items["Bananas"], 1)
        self.assertEqual(result, "Bananas added to the shop")

    def test_remove_item_success(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Bananas", 1)
        self.assertEqual(result, "1 Bananas removed from the shop")

    def test_remove_item_unsuccessful(self):
        self.fresh_shop.add_item("Bananas")
        result = self.fresh_shop.remove_item("Tomatoes", 2)
        self.assertEqual(result, "Cannot remove 2 Tomatoes")

    def test_repr(self):
        self.assertEqual(repr(self.fresh_shop), "Fresh Shop of type Fruit and Veg with capacity 50")


if __name__ == "__main__":
    unittest.main()



