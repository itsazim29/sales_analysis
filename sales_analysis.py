import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/AnudipAE/DANLC/master/cleaned.csv'
dataset = pd.read_csv(url)

print(dataset.head())

print(dataset.shape)

print(dataset.isnull().sum())

print(dataset.describe())

print(dataset.nunique())

# year-wise sales
dataset.groupby('year')['amount'].count().plot(kind='bar', title='Year Wise Sales')
plt.xlabel('Year')
plt.ylabel('Sales Count')
plt.show()

# data for years 2015 to 2018
dataset_2015_2018 = dataset[(dataset['year'] >= 2015) & (dataset['year'] <= 2018)]

# month-wise sales
dataset_2015_2018.groupby('month')['rating'].count().plot(kind='bar', title='Month Wise Sales (2015-2018)')
plt.xlabel('Month')
plt.ylabel('Sales Count')
plt.show()

# top 10 selling brands
dataset_2015_2018.groupby('brand')['amount'].sum().sort_values(ascending=False).head(10).plot(kind='bar', title='Top 10 Selling Brands (2015-2018)')
plt.xlabel('Brand')
plt.ylabel('Total Sales Amount')
plt.show()

# top 10 selling product categories
dataset_2015_2018.groupby('category')['amount'].sum().sort_values(ascending=False).head(10).plot(kind='bar', title='Top 10 Selling Product Categories (2015-2018)')
plt.xlabel('Category')
plt.ylabel('Total Sales Amount')
plt.show()

# distribution of ratings
sns.countplot(x='rating', data=dataset)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# gender-wise customer distribution
gender_distribution = dataset['gender'].value_counts()
plt.pie(gender_distribution, labels=gender_distribution.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral'])
plt.title('Gender-wise Customer Distribution')
plt.show()

# Save the dataset after analysis
dataset.to_csv('analyzed_sales_data.csv', index=False)