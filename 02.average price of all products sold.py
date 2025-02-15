import numpy as np

sales_data = np.array([[150, 200, 250],  # Sales for Product 1
                       [300, 350, 400],  # Sales for Product 2
                       [100, 150, 200]]) # Sales for Product 3

average_price = sales_data.mean()

print("Average price of all products sold:", average_price)
