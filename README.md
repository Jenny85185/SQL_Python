# SQL_Python
Product Database Management
This Python project demonstrates how to create and manage a simple SQLite database to store product information, including the product name, manufacturer, new price, old price, and the calculated average price.

Features:
Create a database table for products if it doesn't already exist.

Add new products to the table with checks to avoid duplicates.

Automatically calculate the average price of a product when it is added.

Display the data in a readable table format using the tabulate library.

Requirements:
Python 3.x

SQLite3 (Included with Python by default)

tabulate library (for displaying the data in a tabular format)

To install tabulate, you can run:

nginx
Копировать
pip install tabulate
Files:
my_database.db – SQLite database file where product data is stored.

script.py – The Python script that manages the database and performs the operations.

How It Works:
Create Database and Table: If the database my_database.db does not exist, it is created, along with the table products.

Add Product: The function add_product(product_name, manufacturer, new_price, old_price) allows you to add products to the database. It checks if the product already exists to avoid duplicates. It also calculates the average price as the mean of the new_price and old_price and updates this value in the database.

Display Products: After adding products, the program fetches and displays all products stored in the database in a clean, formatted table.

Example Usage:
python
Копировать
add_product('Laptop', 'Dell', 1200.99, 1500.00)
add_product('Smartphone', 'Samsung', 800.50, 950.00)
add_product('Headphones', 'Sony', 150.00, 180.00)
This will add products to the products table, and if a product already exists, it will notify you that the product is already in the database.

Code Overview:
product_exists(product_name, manufacturer): Checks whether a product with the same name and manufacturer already exists in the database.

add_product(product_name, manufacturer, new_price, old_price): Adds a new product to the table and updates the average price.

SQLite Connection: Uses sqlite3 to manage the SQLite database and interact with the products table.

tabulate Library: The tabulate library is used to display the database results in a pretty tabular format.

Example Output:
After running the script, the following output will be displayed:

vbnet
Копировать
Product Laptop added to the database.
Product Smartphone added to the database.
Product Tablet added to the database.
Product Smartwatch added to the database.
Product Laptop by Dell already exists in the database.
Product Headphones added to the database.

Products in the database:
+----+-------------+--------------+------------+------------+---------------+
| ID | Product     | Manufacturer | New Price  | Old Price  | Average Price |
+----+-------------+--------------+------------+------------+---------------+
| 1  | Laptop      | Dell         | 1200.99    | 1500.00    | 1350.495      |
| 2  | Smartphone  | Samsung      | 800.50     | 950.00     | 875.25        |
| 3  | Tablet      | Apple        | 600.00     | 750.00     | 675.00        |
| 4  | Smartwatch  | Garmin       | 250.00     | 300.00     | 275.00        |
| 5  | Headphones  | Sony         | 150.00     | 180.00     | 165.00        |
+----+-------------+--------------+------------+------------+---------------+
License:
This project is open source and available under the MIT License.

