import sqlite3
from tabulate import tabulate  # Import tabulate for pretty table output

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Add column average_price if it does not exist
cursor.execute('''
PRAGMA foreign_keys=off;
''')
cursor.execute('''
PRAGMA foreign_keys=on;
''')

# Create the table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    manufacturer TEXT,
    new_price REAL,
    old_price REAL,
    average_price REAL
)
''')

# Function to check if a product already exists in the table
def product_exists(product_name, manufacturer):
    cursor.execute('''
    SELECT COUNT(*) FROM products WHERE product_name = ? AND manufacturer = ?
    ''', (product_name, manufacturer))  # Parameters for the query
    result = cursor.fetchone()  # Get the count of rows found
    return result[0] > 0  # If more than 0, the product already exists

# Function to add a product to the table, if it doesn't exist yet
def add_product(product_name, manufacturer, new_price, old_price):
    if not product_exists(product_name, manufacturer):  # Check if the product exists
        cursor.execute('''
        INSERT INTO products (product_name, manufacturer, new_price, old_price) 
        VALUES (?, ?, ?, ?)
        ''', (product_name, manufacturer, new_price, old_price))
        conn.commit()
        print(f"Product {product_name} added to the database.")
        # After adding a product, calculate and update average_price
        average_price = (new_price + old_price) / 2
        cursor.execute('''
        UPDATE products 
        SET average_price = ? 
        WHERE product_name = ? AND manufacturer = ?
        ''', (average_price, product_name, manufacturer))
        conn.commit()
    else:
        print(f"Product {product_name} by {manufacturer} already exists in the database.")

# Adding products to the table
add_product('Laptop', 'Dell', 1200.99, 1500.00)   # Adding a laptop
add_product('Smartphone', 'Samsung', 800.50, 950.00)  # Adding a smartphone
add_product('Tablet', 'Apple', 600.00, 750.00)      # Adding a tablet
add_product('Smartwatch', 'Garmin', 250.00, 300.00)  # Adding a smartwatch
add_product('Laptop', 'Dell', 1200.99, 1500.00)     # Trying to add a duplicate product

# Add a new product here
add_product('Headphones', 'Sony', 150.00, 180.00)  # Adding a new product (Headphones by Sony)

# Execute the SQL query to select all data from the products table
cursor.execute('SELECT * FROM products')

# Fetch all the rows from the result
rows = cursor.fetchall()

# Print the result as a table
print("\nProducts in the database:")
print(tabulate(rows, headers=["ID", "Product", "Manufacturer", "New Price", "Old Price", "Average Price"], tablefmt="pretty"))


cursor.close()
conn.close()
