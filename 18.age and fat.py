import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Sample data
data = {
    'age': [23, 45, 34, 50, 26, 31, 42, 37, 29, 48, 36, 38, 33, 40, 27, 52, 30, 35],
    'body_fat': [15, 22, 18, 25, 12, 14, 19, 17, 13, 24, 16, 20, 15, 21, 11, 26, 14, 19]
}
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = np.mean(df['age'])
median_age = np.median(df['age'])
std_age = np.std(df['age'])

mean_fat = np.mean(df['body_fat'])
median_fat = np.median(df['body_fat'])
std_fat = np.std(df['body_fat'])

print("Mean Age:", mean_age, " | Median Age:", median_age, " | Std Age:", std_age)
print("Mean Body Fat:", mean_fat, " | Median Body Fat:", median_fat, " | Std Body Fat:", std_fat)

# Boxplots
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['age', 'body_fat']])
plt.title('Boxplots for Age and Body Fat')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['body_fat'])
plt.title('Scatter Plot: Age vs Body Fat')
plt.xlabel('Age')
plt.ylabel('Body Fat (%)')
plt.grid(True)
plt.show()

# Q-Q Plot
stats.probplot(df['body_fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Body Fat')
plt.show()
