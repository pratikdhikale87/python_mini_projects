from Inventory import Product


class InventoryController:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price, quantity, reorder_level):
        product = Product(product_id, name, price, quantity, reorder_level)
        self.products[product_id] = product
        print("Product added successfully")

    def purchase_product(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.add_stock(quantity)
            print("Stock updated")
        else:
            print("Product not found")

    def sell_product(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            if product.remove_stock(quantity):
                print("Sale successful")
            else:
                print("Insufficient stock")
        else:
            print("Product not found")

    def view_inventory(self):
        print("\n--- Inventory ---")
        for product in self.products.values():
            print(f"ID:{product.product_id} | "
                  f"{product.name} | "
                  f"Qty:{product.quantity} | "
                  f"Price:{product.price}")
            if product.is_low_stock():
                print("Low stock alert!")
