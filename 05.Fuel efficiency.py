import numpy as np

fuel_efficiency = np.array([25, 30, 35, 40, 45])
average_efficiency = fuel_efficiency.mean()
percentage_improvement = ((fuel_efficiency[4] - fuel_efficiency[0]) / fuel_efficiency[0]) * 100
print("Average fuel efficiency:", average_efficiency)
print("Percentage improvement between model 1 and model 5:", percentage_improvement)
