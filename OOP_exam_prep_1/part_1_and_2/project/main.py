# Initialize the FactoryManager
from project.factory_manager import FactoryManager

factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))
