
# Import necessary libraries
import pandas as pd
from collections import Counter

# Sample DataFrame (Replace this with your actual data)
# Assuming the DataFrame is named sales_data and has a column 'customer_age'
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_age': [25, 30, 22, 25, 30, 28, 22, 25, 35, 30]
}
sales_data = pd.DataFrame(data)

# Calculate frequency distribution of customer ages
age_freq = Counter(sales_data['customer_age'])

# Display the frequency distribution
for age, freq in age_freq.items():
    print(f'Age {age}: {freq} purchases')
