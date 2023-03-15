import os
import pandas as pd

# Get a list of all csv files in the folder
folder_path = 'bike_data/2020-2021'
csv_files = []

for files in os.listdir(folder_path):
    if files.endswith('.csv'):
        csv_files.append(os.path.join(folder_path,files))
        
print(csv_files)
 
# Combine all csv into a single dataframe
df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)

# Write the combined Dataframe to a new CSV file
df.to_csv('bike_data/2020-2021/merged_data/merged.csv', index=False)