import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01', '2023-06-01'],
    'Temperature (Celsius)': [25, 28, 30, 32, 35, 38]
}
temperature_data = pd.DataFrame(data)

# Convert 'Date' column to datetime
temperature_data['Date'] = pd.to_datetime(temperature_data['Date'])

# Calculate average temperature for each month
temperature_data['Month'] = temperature_data['Date'].dt.to_period('M')
avg_temp_by_month = temperature_data.groupby('Month')['Temperature (Celsius)'].mean()

# Display the results
print("Average Temperature by Month:\n", avg_temp_by_month)

# Line chart for temperature trend
avg_temp_by_month.plot(kind='line', figsize=(10, 6), marker='o', linestyle='-')
plt.title('Temperature Trend Over Time')
plt.xlabel('Month')
plt.ylabel('Average Temperature (Celsius)')
plt.grid(True)
plt.show()
