import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2],
    'order_date': ['2024-01-01', '2024-01-03', '2024-01-05', '2024-01-07', '2024-01-10'],
    'product_name': ['A', 'B', 'A', 'C', 'B'],
    'order_quantity': [2, 1, 3, 5, 2]
})

order_data['order_date'] = pd.to_datetime(order_data['order_date'])
orders_by_customer = order_data.groupby('customer_id').size()
avg_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order = order_data['order_date'].min()
latest_order = order_data['order_date'].max()
print("Total Orders by Each Customer:\n", orders_by_customer)
print("\nAverage Order Quantity for Each Product:\n", avg_order_quantity_per_product)
print("\nEarliest Order Date:", earliest_order)
print("Latest Order Date:", latest_order)
