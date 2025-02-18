# Import necessary libraries
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

# Download NLTK stopwords (only needed once)
nltk.download('stopwords')

# Load stop words
stop_words = set(stopwords.words('english'))

# Load the dataset from CSV file
data = pd.read_csv('data.csv')

# Preprocess the text data
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Split text into words
    words = text.split()
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    return words

# Apply preprocessing to all feedback entries
all_words = []
for feedback in data['feedback']:
    all_words.extend(preprocess_text(feedback))

# Calculate frequency distribution of words
word_freq = Counter(all_words)

# Get user input for top N words
N = int(input("Enter the number of top frequent words to display: "))

# Get the top N most frequent words
top_n_words = word_freq.most_common(N)

# Display the top N most frequent words and their frequencies
print("\nTop", N, "most frequent words:")
for word, freq in top_n_words:
    print(f'{word}: {freq}')

# Plot a bar graph to visualize the top N most frequent words
words, frequencies = zip(*top_n_words)
plt.figure(figsize=(12, 6))
plt.bar(words, frequencies, color='purple')
plt.title('Top {} Most Frequent Words'.format(N))
plt.xlabel('Words')
plt.ylabel('Frequencies')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
