from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)
        self.sells = "Toys"


    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        result += self.get_estimated_profit() + "\n"
        result += "**Toys for sale:\n"

        details = {}

        for p in self.products:
            if p.model not in details:
                details[p.model] = {"count": 0, "total_price": 0}
            details[p.model]["count"] += 1
            details[p.model]["total_price"] += p.price

        for model in sorted(details):
            stats = details[model]
            avg_price = stats["total_price"] / stats["count"]
            result += f"{model}: {stats['count']}pcs, average price: {avg_price:.2f}\n"
        return result[:-1]