# Imports
import pandas as pd
import os
import glob

# Go to the folder and collect in list all files witch extension equals to '.csv'
os.chdir("Path to folder, where scraped data are storing")
files = [i for i in glob.glob('*.{}'.format('csv'))]

# Remove file 'appearances.csv' because this file contain every player which played during this season
# This data frame will be my basis. I will later merge 'data' with next data frames
files.remove('appearances.csv')
data = pd.read_csv('Path to file appearances.csv'
                   , names = ['player', 'appearances'])

# Merge with 'data' every csv file in list
for file in files:
    temporary_data = pd.read_csv(file, names=['player', str(file)[:-4]])
    data = pd.merge(data, temporary_data, on=['player'], how = 'left')

# NaNs to 0s
data.fillna(0, inplace=True)

# In some columns are values like 1,000 instead of 1000
data.replace(',', '', regex=True, inplace=True)

# Aerials won + aerials lost = aerial fights attempts
data["aerial_attempts"] = data['aerial_lost'] + data['aerial_won']

# Making player column as an index column
data.index = data['player']
data.pop('player')

# Types of each column
print(data.dtypes)

# Almost every column is float and some are objects
# This loop below convert every one to an int
for column in data:
    data[column] = data[column].astype(int)


# Export data frame to csv file
export_csv = data.to_csv('Premier_League_Forwards_Data_In_Current_Season_So_Far.csv'
                         , index=True, header=True)
