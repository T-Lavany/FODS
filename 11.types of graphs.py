# Import necessary libraries
import matplotlib.pyplot as plt

# Sample data
days = list(range(1, 31))  # Days of the month
sales = [100, 120, 90, 110, 150, 130, 170, 160, 180, 200, 
         190, 210, 220, 200, 230, 240, 250, 270, 260, 280, 
         300, 290, 310, 320, 330, 340, 350, 360, 370, 380]

# 1. Line plot
plt.figure(figsize=(10, 6))
plt.plot(days, sales, marker='o', linestyle='-', color='blue', label='Sales')
plt.title('Sales Trend Over a Month')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()

# 2. Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(days, sales, color='red', label='Sales')
plt.title('Sales Scatter Plot Over a Month')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()

# 3. Bar plot
plt.figure(figsize=(10, 6))
plt.bar(days, sales, color='green', label='Sales')
plt.title('Sales Bar Plot Over a Month')
plt.xlabel('Days')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
