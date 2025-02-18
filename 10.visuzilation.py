import matplotlib.pyplot as plt

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1200, 1300, 1250, 1400, 1550, 1600, 1450, 1500, 1600, 1650, 1700, 1750]

# Line plot
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', color='b', label='Sales')
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()

# Bar plot
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='g', label='Sales')
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()
