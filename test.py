import pandas as pd
import os


csv_file = 'data/data.csv'
data = pd.read_csv(csv_file)
data['Match'] = None  # Add a new column for matches
index = 0  # Track the current index


row = data.iloc[index]
image_url = row['Image']  # Image URL column in CSV
name = row['Name']  # Name column
account_id = row['Account_ID']  # Account_ID column

print(image_url)
print(name)
print(account_id)