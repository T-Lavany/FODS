# Import necessary libraries
import pandas as pd
from collections import Counter
import re

# Sample DataFrame (Replace this with your actual data)
# Assuming the DataFrame is named reviews_data and has a column 'review_text'
data = {
    'review_id': [1, 2, 3, 4, 5],
    'review_text': [
        "Great product! Highly recommend it.",
        "Not worth the price. Quality could be better.",
        "Excellent product, very satisfied with the purchase.",
        "Good value for money. Would buy again.",
        "Terrible experience. The product broke after one use."
    ]
}
reviews_data = pd.DataFrame(data)

# Concatenate all reviews into a single text
all_reviews = " ".join(reviews_data['review_text'].tolist())

# Preprocess the text: Convert to lowercase and remove punctuation
all_reviews = all_reviews.lower()
all_reviews = re.sub(r'[^\w\s]', '', all_reviews)

# Split text into words
words = all_reviews.split()

# Calculate frequency distribution of words
word_freq = Counter(words)

# Display the frequency distribution
for word, freq in word_freq.items():
    print(f'{word}: {freq}')
