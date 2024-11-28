from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    MATERIAL = "Wood"
    SUB_TYPE = "Furniture"

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material=self.MATERIAL, sub_type=self.SUB_TYPE)

    def discount(self):
        self.price -= self.price * 0.10