# Import necessary libraries
import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 32, 35, 38, 40, 42, 43, 41, 38, 35, 32, 30]  # Average monthly temperatures
rainfall = [50, 40, 60, 80, 100, 120, 150, 130, 110, 90, 70, 60]  # Monthly rainfall in mm

# 1. Line plot for monthly temperature
plt.figure(figsize=(10, 6))
plt.plot(months, temperature, marker='o', linestyle='-', color='orange', label='Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Scatter plot for monthly rainfall
plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall, color='blue', label='Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.legend()
plt.show()
