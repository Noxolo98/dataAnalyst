#importing important libraries for data analysis and visualization
import pandas as pd #for data manipulation
import matplotlib.pyplot as plt #for creating plots and visualization
import numpy as np #for numerical operation
#loading the data set to pandas dataframe
df = pd.read_csv('housing_prices.csv')
df['price'] = df['price'] / 1e6
# Display basic information about the DataFrame, such as columns, data types, and non-null values
print(df.info())

print(df.isnull().sum()) #check for missing values
df['price'] = df['price'].fillna(df['price'].mean()) #fill in the missing values in the price column
df = df.drop_duplicates() #drop duplicates from dataframe
print(df['price'].mean())
print(df['bedrooms'].value_counts())
avg_price_by_bedrooms = df.groupby('bedrooms')['price'].mean()
#create a scatter plot showing relationship between house prices and bedrooms
avg_price_by_bedrooms.plot(kind='bar', title='Average Price by bedrooms (in millions)', color='skyblue')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Average Price (in millions)')
plt.show()
# Filter the data to include only houses with more than 3 bedrooms
filtered_data = df[df['bedrooms'] > 3]


