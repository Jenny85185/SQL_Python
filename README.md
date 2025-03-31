# SQL_Python
# Product Database Script

## Description

This Python script connects to a SQLite database and manages a list of products. The script includes functionality for adding products to the database, checking if a product already exists, and calculating an average price for each product. The script also prints the list of products in a nice, tabular format.

## Features

- **Product Management**: Add products to the database.
- **Average Price Calculation**: Automatically calculates and updates the average price of a product based on the new and old price.
- **SQLite Database**: Uses SQLite to store product information.
- **Tabular Output**: Displays products in a formatted table using the `tabulate` library.

## How It Works

1. The script connects to a SQLite database (it will be created if it doesn't exist).
2. It ensures the `products` table is present.
3. The script includes a check for duplicates, so products will only be added if they don't already exist in the database.
4. The `average_price` is calculated as the average of `new_price` and `old_price` for each product.
5. The products are displayed in a nicely formatted table.

## Requirements

- Python 3.x
- SQLite
- `tabulate` library (install via `pip install tabulate`)

## Usage

1. Run the script. It will automatically add products to the database and calculate average prices.
2. You can modify the product details or add new products as needed.
3. The product information will be displayed as a table.

## Example

Here is an example of how products will appear:

| ID  | Product    | Manufacturer | New Price | Old Price | Average Price |
|-----|------------|--------------|-----------|-----------|---------------|
| 1   | Laptop     | Dell         | 1200.99   | 1500.00   | 1350.50       |
| 2   | Smartphone | Samsung      | 800.50    | 950.00    | 875.25        |
| 3   | Tablet     | Apple        | 600.00    | 750.00    | 675.00        |
| 4   | Smartwatch | Garmin       | 250.00    | 300.00    | 275.00        |
| 5   | Headphones | Sony         | 150.00    | 180.00    | 165.00        |

## Conclusion

This script helps manage a simple product database, ensuring that new products are added only if they don't already exist, and it provides a clear and user-friendly way of viewing the data.
