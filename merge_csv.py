import os
import pandas as pd

# Get a list of all csv files in the folder
folder_path = os.getcwd()
csv_files = []

for files in os.listdir(folder_path):
    if files.endswith('.csv'):
        csv_files.append(os.path.join(folder_path,files))
        
print(csv_files)
 
# Combine all csv into a single dataframe
df = pd.concat((pd.read_csv(f) for f in csv_files), ignore_index=True)

# Create a directory called 'merged_data' in the current working directory if it doesn't exist
dir_path = os.path.join(os.getcwd(), 'merged_data')

# Write the combined Dataframe to a new CSV file
output_path = os.path.join(dir_path, 'merged.csv')
df.to_csv(output_path, index=False)