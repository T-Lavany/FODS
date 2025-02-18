# Import necessary libraries
import pandas as pd
from collections import Counter

# Sample DataFrame (Replace this with your actual data)
# Assuming the DataFrame is named interaction_data and has a column 'likes'
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [10, 15, 10, 20, 15, 25, 30, 10, 20, 25]
}
interaction_data = pd.DataFrame(data)

# Calculate frequency distribution of likes
likes_freq = Counter(interaction_data['likes'])

# Display the frequency distribution
for likes, freq in likes_freq.items():
    print(f'Posts with {likes} likes: {freq}')
