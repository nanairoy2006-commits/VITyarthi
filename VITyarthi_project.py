class Product:
    def __init__(self, product_id, name, price, quantity, restock_threshold):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.restock_threshold = restock_threshold
        self.sales = 0

    def buy(self, amount):
        if amount > self.quantity:
            print(f"Sorry, only {self.quantity} units of {self.name} available.")
            return False
        self.quantity -= amount
        self.sales += amount * self.price
        print(f"Purchased {amount} units of {self.name}.")
        if self.quantity < self.restock_threshold:
            print(f"Restock alert for {self.name}! Only {self.quantity} units left.")
        return True

    def details(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def show_inventory(self):
        print("Current Inventory:")
        for product in self.products.values():
            print(product.details())

    def purchase(self, product_id, amount):
        if product_id in self.products:
            self.products[product_id].buy(amount)
        else:
            print("Product ID not found.")

    def sales_summary(self):
        print("Sales Summary:")
        for product in self.products.values():
            print(f"{product.name}: ₹{product.sales}")
        total_sales = sum(p.sales for p in self.products.values())
        print(f"\nTotal Sales: ₹{total_sales}")

# Example usage:
store = Store()
store.add_product(Product(101, "Laptop", 50000, 10, 2))
store.add_product(Product(102, "Headphones", 1500, 20, 5))
store.add_product(Product(103, "Keyboard", 700, 15, 3))

store.show_inventory()

store.purchase(101, 2)
store.purchase(102, 1)
store.purchase(103, 13)

store.show_inventory()

store.sales_summary()
