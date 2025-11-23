# VITyarthi

Project Explanation
The project is designed to solve a real problem faced by small e-commerce retailers: unexpected stock-outs due to poor inventory tracking. The tool helps store managers:

Track the inventory (how many items of each product are in stock)

Automate purchase handling (customers can buy products, which reduces that product’s stock)

Generate restock alerts (notifies when product stock drops below a critical level)

Summarize sales (total sales figures per product)

The goal is to reduce lost sales and improve decision-making by making inventory and sales data always available and up to date.

Python Code Explanation
The solution is modular, using classes for both products and the store:

1. Product Class
Attributes: product ID, name, price, quantity in stock, threshold for restocking, and sales made.

Methods:

reduce_stock(amount): Tries to reduce the stock if there’s enough available.

needs_restock(): Returns True if stock is below the threshold, signaling a restock alert.

2. Store Class
Attributes: a collection (dictionary) of all products.

Methods:

add_product(product): Adds a product to the inventory.

show_inventory(): Prints all products with their current quantities.

purchase(product_id, amount): Processes a sale, updates inventory, checks for restock alerts.

sales_summary(): Prints total sales per product.

3. Usage Workflow (main() function)
Create a Store object.

Add multiple Product objects (e.g., Laptop, Mouse, Mobile).

Show the starting inventory.

Conduct sample purchase transactions.

Show updated inventory and sales summary.

Automatic alerts are printed when any product’s stock drops below its restock level.

