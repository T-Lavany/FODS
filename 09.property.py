import pandas as pd

data = {
    "Location": ["Location1", "Location2", "Location1", "Location3", "Location2"],
    "Listing_Price": [500000, 750000, 600000, 850000, 720000],
    "Bedrooms": [3, 5, 4, 6, 2],
    "Area": [2000, 3500, 1800, 4000, 2500]
}

property_data = pd.DataFrame(data)

avg_price_per_location = property_data.groupby("Location")["Listing_Price"].mean()
properties_with_more_than_4_bedrooms = len(property_data[property_data["Bedrooms"] > 4])
largest_area_property = property_data.loc[property_data["Area"].idxmax()]

print(avg_price_per_location)
print(properties_with_more_than_4_bedrooms)
print(largest_area_property)
