class Product:
    def __init__(self, product_id, name, price, quantity, reorder_level):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.reorder_level = reorder_level

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            return True
        return False

    def is_low_stock(self):
        return self.quantity <= self.reorder_level
