from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    product_types = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    store_types = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name):
        self.name = name
        self.income = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.product_types:
            raise Exception("Invalid product type!")

        product = self.product_types[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.store_types:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.store_types[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        filtered_products = [p for p in products if p.sub_type == store.sells]

        if not filtered_products:
            return f"Products do not match in type. Nothing sold."

        for p in filtered_products:
            store.products.append(p)
            store.capacity -= 1
            self.products.remove(p)
            self.income += p.price

        return (f"Store {store.name} successfully purchased "
                f"{len(filtered_products)} items.")

    def unregister_store(self, store_name: str):
        try:
            store = [s for s in self.stores if s.name == store_name][0]
        except IndexError:
            raise Exception("No such store!")

        if store.products:
            return f"The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        filtered_products = [p for p in self.products if p.model == product_model]
        for p in filtered_products:
            p.discount()
        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        try:
            store = [s for s in self.stores if s.name == store_name][0]
        except IndexError:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        result = f"Factory: {self.name}\n"
        result += f"Income: {self.income:.2f}\n"
        result += "***Products Statistics***\n"

        product_stats = {}
        for p in self.products:
            if p.model not in product_stats:
                product_stats[p.model] = 0
            product_stats[p.model] += 1

        result += (f"Unsold Products: {len(self.products)}. "
                   f"Total net price: {sum([p.price for p in self.products]):.2f}\n")

        ordered_products = sorted(product_stats)
        for model in ordered_products:
            result += f"{model}: {product_stats[model]}\n"

        result += f"***Partner Stores: {len(self.stores)}***\n"
        store_names = '\n'.join(sorted([s.name for s in self.stores]))
        result += store_names
        return result
