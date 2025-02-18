import pandas as pd

# Sample Data for Orders
orders_data = pd.DataFrame({
    'Order ID': [1, 2, 3, 4, 5],
    'Customer ID': [101, 102, 103, 101, 104],
    'Order Date': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-02-01', '2023-02-15']
})

# Sample Data for Customer Info
customer_info = pd.DataFrame({
    'Customer ID': [101, 102, 103, 104, 105],
    'Name': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis'],
    'Email': ['john@example.com', 'jane@example.com', 'alice@example.com', 'bob@example.com', 'charlie@example.com'],
    'Phone Number': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123', '567-890-1234']
})

# Merge data frames on 'Customer ID'
merged_data = pd.merge(orders_data, customer_info, on='Customer ID')

# Calculate time between consecutive orders
merged_data['Order Date'] = pd.to_datetime(merged_data['Order Date'])
merged_data.sort_values(by=['Customer ID', 'Order Date'], inplace=True)
merged_data['Time Between Orders'] = merged_data.groupby('Customer ID')['Order Date'].diff().dt.days

# Calculate average time between orders
avg_time_between_orders = merged_data['Time Between Orders'].mean()

print("Merged Data with Time Between Orders:\n", merged_data)
print("\nAverage time between consecutive orders:", avg_time_between_orders)
