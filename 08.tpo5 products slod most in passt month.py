import pandas as pd

sales_data = pd.DataFrame({
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'E', 'A', 'B'],
    'order_date': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05', 
                   '2024-10-06', '2024-10-07', '2024-10-08', '2024-10-09', '2024-10-10'],
    'quantity_sold': [10, 5, 7, 3, 8, 6, 2, 4, 9, 11]
})

sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])

top_products = sales_data.groupby('product_name')['quantity_sold'].sum().sort_values(ascending=False).head(5)

print(top_products)
