import pandas as pd

# Loading Dataset
ds = pd.read_csv("D:/MachineLearning/datasets/hw1/earth_surface_temperatures.csv")

# Q1a. Identify and rectify any missing values in the data using appropriate techniques.
print(ds.isna().sum())

# Q1b. Transform the Years and Month columns into a single column labeled "Date" in
# the MM-YYYY format, with a datetime64[ns] data type
ds['Date'] = pd.to_datetime(ds[['Month','Years']].assign(Day=1))
ds['Date'] = ds['Date'].dt.strftime('%m-%Y')
print(ds.head())

# Q1c. Detect and investigate extreme temperature values that might be regarded as outliers
print(ds.Temperature.unique())

ds.describe()