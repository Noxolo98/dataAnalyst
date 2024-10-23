Housing Price Analysis Report
Prepared by: Noxolo Luswazi
Date: October 2024
1. Introduction
This report provides an analysis of housing prices based on a dataset that contains information about properties, including the number of bedrooms, price, and area. The analysis aims to:

Understand key statistical properties of the dataset.
Explore the relationship between the number of bedrooms and house prices.
Visualize housing price patterns using a bar graph.
Handle missing data and outliers, if any, to ensure data accuracy.
2. Data Overview
The dataset, housing_prices.csv, contains the following features:

Price: The price of each property (initially in the local currency but converted to millions for analysis).
Bedrooms: The number of bedrooms in each house.
Area: The geographical area of the property.
The data cleaning process involved handling missing values, removing duplicates, and converting prices into millions for easier interpretation.

3. Data Preprocessing
3.1 Handling Missing Values
Missing values in the price column were handled by filling them with the mean of the column.
There were no missing values in the bedrooms column.
3.2 Removing Duplicates
Duplicate rows in the dataset were identified and removed to ensure that each property was uniquely represented.
3.3 Converting Prices to Millions
The prices were originally in their full amounts. To make the analysis more intuitive, the prices were divided by 1,000,000 to convert them into millions.
4. Exploratory Data Analysis
4.1 Descriptive Statistics
The dataset's basic descriptive statistics were calculated to provide insights into the data distribution. These statistics included the mean, standard deviation, minimum, and maximum values for numerical columns.
For example, the average price of a house in the dataset (after missing values were handled and duplicates were removed) was calculated as:

Mean House Price: X million
4.2 Bedroom Distribution
The number of bedrooms in the dataset ranged from 1 to X bedrooms. The frequency of properties with a given number of bedrooms was calculated, showing that the majority of houses had X bedrooms.

5. Visualization of Relationships
5.1 Average Price by Number of Bedrooms
To explore the relationship between the number of bedrooms and house prices, a bar graph was plotted. The graph showed the average price for properties with different bedroom counts.

Key Findings:
Properties with more bedrooms generally had higher average prices.
The average price of houses with X bedrooms was Y million.


5.2 Price Per Bedroom
A new feature, price per bedroom, was calculated by dividing the house price by the number of bedrooms. This gave insight into how much price was attributed to each additional bedroom.


6. Conclusion
This analysis provided valuable insights into the relationship between housing prices and key property features such as the number of bedrooms and location. Key findings include:

Properties with more bedrooms tend to have higher average prices, but this varies based on location.
 
