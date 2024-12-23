import pandas as pd

# Load the dataset
df = pd.read_csv('airbnb_listings.csv')

# Display the first few rows of the dataset to inspect
print(df.head())




# Check the structure of the dataset: data types and missing values
print(df.info())

# Check for missing values in each column
print(df.isnull().sum())



# Drop rows with missing values
df_cleaned = df.dropna()

# Check if any missing values remain
print(df_cleaned.isnull().sum())



# Fill missing values with the mean of each column (for numerical columns)
df['Units Sold'] = df['Units Sold'].fillna(df['Units Sold'].mean())
df['Revenue'] = df['Revenue'].fillna(df['Revenue'].mean())

# Fill missing values in a categorical column (e.g., 'Product') with the mode (most frequent value)
df['Product'] = df['Product'].fillna(df['Product'].mode()[0])

# Check if any missing values remain
print(df.isnull().sum())


# Compute basic statistics for the numerical columns
print(df.describe())


# Group by the 'Region' column and compute the mean for 'Units Sold' and 'Revenue'
region_group = df.groupby('Region')[['Units Sold', 'Revenue']].mean()

# Display the grouped results
print(region_group)


import matplotlib.pyplot as plt
import seaborn as sns

# Create a boxplot for units sold by region
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Units Sold', data=df)
plt.title('Boxplot of Units Sold by Region')
plt.show()

# Create a scatter plot of Units Sold vs. Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units Sold', y='Revenue', data=df)
plt.title('Units Sold vs. Revenue')
plt.show()



import matplotlib.pyplot as plt
import pandas as pd

# Assuming 'Date' is already in datetime format, if not, convert it
df['Date'] = pd.to_datetime(df['Date'])

# Group by Date and sum the 'Units Sold' or 'Revenue' for each day
daily_sales = df.groupby('Date')['Units Sold'].sum()

# Plotting the Line Chart
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='b')
plt.title('Daily Sales Trend Over Time', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Units Sold', fontsize=12)
plt.xticks(rotation=45)  # Rotate the x-axis labels for better visibility
plt.grid(True)
plt.tight_layout()
plt.show()



import seaborn as sns

# Grouping by Region and calculating the mean of 'Units Sold'
region_avg_sales = df.groupby('Region')['Units Sold'].mean().reset_index()

# Plotting the Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Units Sold', data=region_avg_sales, palette='viridis')
plt.title('Average Units Sold by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Average Units Sold', fontsize=12)
plt.tight_layout()
plt.show()




# Plotting the Histogram for 'Revenue'
plt.figure(figsize=(10, 6))
plt.hist(df['Revenue'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Revenue', fontsize=16)
plt.xlabel('Revenue', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()




# Plotting the Scatter Plot between 'Units Sold' and 'Revenue'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Units Sold', y='Revenue', data=df, color='orange', alpha=0.6)
plt.title('Units Sold vs Revenue', fontsize=16)
plt.xlabel('Units Sold', fontsize=12)
plt.ylabel('Revenue', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

