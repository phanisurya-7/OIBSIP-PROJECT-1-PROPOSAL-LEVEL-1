import pandas as pd

# Load the dataset
df = pd.read_csv('retail_sales.csv')

# Inspect the dataset
print(df.head())
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Fill or drop missing values
df = df.fillna(0)  # Example: Replace missing values with 0
print(df.describe())
print(df['column_name'].value_counts())  # Replace 'column_name' with a relevant column
df['date'] = pd.to_datetime(df['date_column'])  # Replace 'date_column' with the date column name
df = df.sort_values('date')

# Plot sales over time
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['sales_column'], label='Sales')  # Replace 'sales_column'
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()
# Group by product or category
product_sales = df.groupby('product_column')['sales_column'].sum()  # Replace column names
print(product_sales)

# Analyze customer demographics (if available)
customer_analysis = df.groupby('customer_column').agg({'sales_column': 'sum', 'order_column': 'count'})
print(customer_analysis)
import seaborn as sns

# Bar plot for product sales
sns.barplot(x='product_column', y='sales_column', data=df)  # Replace column names
plt.title('Sales by Product')
plt.show()

# Heatmap for correlations
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Feature Correlation')
plt.show()

