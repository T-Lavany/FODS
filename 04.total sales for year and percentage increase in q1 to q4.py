import numpy as np

sales_data = np.array([50000, 60000, 70000, 90000])
total_sales = sales_data.sum()
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Total sales for the year:", total_sales)
print("Percentage increase from Q1 to Q4:", percentage_increase)
