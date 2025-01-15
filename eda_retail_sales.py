import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
retail_data = pd.read_csv('eda_retail_sales.csv')

# Display dataset head and info
print("Dataset Head:")
print(retail_data.head())
print("\nDataset Info:")
print(retail_data.info())

# Check for missing values
print("\nMissing Values:")
print(retail_data.isnull().sum())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(retail_data.describe())

# Gender Distribution
print("\nGender Distribution:")
print(retail_data['Gender'].value_counts())

# Product sales (total amount per product category)
print("\nProduct Sales:")
product_sales = retail_data.groupby('Product Category')['Total Amount'].sum()
print(product_sales)

# Convert Date to datetime type
retail_data['Date'] = pd.to_datetime(retail_data['Date'])

# Time Series Analysis (Sales Over Time)
plt.figure(figsize=(12, 6))
retail_data.groupby('Date')['Total Amount'].sum().plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Correlation Matrix (Numeric Columns Only)
numeric_data = retail_data.select_dtypes(include=['number'])  # Select only numeric columns
correlation = numeric_data.corr()  # Calculate correlation matrix
print("\nCorrelation Matrix:")
print(correlation)

# Plot Heatmap for Correlation
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()

# Visualizing Sales by Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=retail_data, palette='Set2')
plt.title('Sales by Gender')
plt.show()

# Product-wise Sales Visualization (Bar plot)
plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.index, y=product_sales.values, palette='viridis')
plt.title('Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()

