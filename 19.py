import pandas as pd

# Sample Data
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Product': ['A', 'B', 'C', 'A', 'C'],
    'Quantity Sold': [10, 15, 5, 20, 10],
    'Unit Price': [100, 150, 200, 100, 200]
}
sales_data = pd.DataFrame(data)

# Create 'Total Sales' column
sales_data['Total Sales'] = sales_data['Quantity Sold'] * sales_data['Unit Price']

# Total sales for each product
total_sales_by_product = sales_data.groupby('Product')['Total Sales'].sum()

# Overall profit (20% profit margin)
sales_data['Profit'] = sales_data['Total Sales'] * 0.2
total_profit_by_product = sales_data.groupby('Product')['Profit'].sum()

# Top 5 most profitable products
top_5_profitable = total_profit_by_product.sort_values(ascending=False).head(5)

print("Total Sales by Product:\n", total_sales_by_product)
print("\nTop 5 Most Profitable Products:\n", top_5_profitable)
