import pandas as pd

# Sample Data
data = {
    'Customer ID': [1, 2, 3, 4, 5],
    'Age': [25, 30, 22, 35, 28],
    'Gender': ['M', 'F', 'M', 'F', 'M'],
    'Total Spending': [1200, 800, 300, 1500, 600]
}
customer_data = pd.DataFrame(data)

# Segment customers
conditions = [
    (customer_data['Total Spending'] > 1000),
    (customer_data['Total Spending'] > 500) & (customer_data['Total Spending'] <= 1000),
    (customer_data['Total Spending'] <= 500)
]
choices = ['High Spenders', 'Medium Spenders', 'Low Spenders']
customer_data['Spending Segment'] = pd.cut(customer_data['Total Spending'], bins=[0, 500, 1000, float('inf')], labels=choices)

# Average age in each segment
avg_age_by_segment = customer_data.groupby('Spending Segment')['Age'].mean()

print("Customer Data with Segments:\n", customer_data)
print("\nAverage Age by Spending Segment:\n", avg_age_by_segment)
