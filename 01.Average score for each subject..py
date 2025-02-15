import numpy as np

scores = np.array([[85, 90, 78, 92],
                   [88, 85, 80, 85],
                   [90, 91, 84, 88],
                   [78, 85, 76, 89]])

averages = scores.mean(axis=0)
subject = ['Math', 'Science', 'English', 'History'][np.argmax(averages)]

print("Averages:", averages)
print("Highest:", subject)
