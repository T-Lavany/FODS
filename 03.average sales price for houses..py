import numpy as np
house_data = np.array([[3, 1500, 250000],
                       [5, 3000, 450000],
                       [4, 2000, 350000],
                       [6, 4000, 550000]])
houses_with_4_plus_bedrooms = house_data[house_data[:, 0] > 4]
average_price = houses_with_4_plus_bedrooms[:, 2].mean()
print("Average sale price of houses with more than 4 bedrooms:", average_price)
