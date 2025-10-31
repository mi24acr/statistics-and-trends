# ================================================
# Applied Data Science 1 – Statistics and Trends Assignment
# Student Name: Muhammad Hassan Iqbal Bhatti
# Student ID: 23100172
# Tutor: Dr. William Cooper
# Submission Date: 23-OCT-2022
# ================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# 1. Load Dataset
# =============================
data = pd.read_csv('shopping_trends.csv')
print("Dataset loaded successfully! Shape:", data.shape)

# Display basic info
data.info()

# =============================
# 2. Data Cleaning and Preparation
# =============================
# Drop duplicates and missing values
data = data.drop_duplicates().dropna()

# Convert appropriate columns to categorical type
categorical_cols = ['Gender', 'Category', 'Payment Method']
for col in categorical_cols:
    if col in data.columns:
        data[col] = data[col].astype('category')

# =============================
# 3. Descriptive Statistics & Statistical Moments
# =============================
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

for col in numeric_cols:
    print(f"\nStatistics for {col}:")
    print(f"Mean: {data[col].mean():.2f}")
    print(f"Variance: {data[col].var():.2f}")
    print(f"Skewness: {data[col].skew():.2f}")
    print(f"Kurtosis: {data[col].kurt():.2f}")

# =============================
# 4. Relational Plot – Line Plot (Spending vs Age)
# =============================
if 'Age' in data.columns and 'Purchase Amount (USD)' in data.columns:
    plt.figure(figsize=(8, 5))
    sns.lineplot(x='Age', y='Purchase Amount (USD)', data=data, color='teal')
    plt.title('Relational Plot: Average Spending vs Age')
    plt.xlabel('Customer Age')
    plt.ylabel('Purchase Amount (USD)')
    plt.tight_layout()
    plt.savefig('relational_plot_line.png')
    plt.show()

# =============================
# 5. Categorical Plot – Pie Chart (Gender Distribution)
# =============================
if 'Gender' in data.columns:
    gender_counts = data['Gender'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Categorical Plot: Gender Distribution of Customers')
    plt.tight_layout()
    plt.savefig('categorical_plot_pie.png')
    plt.show()

# =============================
# 6. Statistical Plot – Box Plot (Purchase by Category)
# =============================
if 'Category' in data.columns and 'Purchase Amount (USD)' in data.columns:
    plt.figure(figsize=(9, 6))
    sns.boxplot(x='Category', y='Purchase Amount (USD)', data=data, palette='coolwarm')
    plt.title('Statistical Plot: Purchase Amount Distribution by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Purchase Amount (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('statistical_plot_box.png')
    plt.show()

# =============================
# 7. Summary Output
# =============================
print("\n===== Summary of Analysis =====")
print("1. Line Plot: Shows average spending trend across different age groups.")
print("2. Pie Chart: Illustrates gender distribution among customers.")
print("3. Box Plot: Reveals variation in purchase amount across categories.")
print("All visual outputs are saved as PNG files for inclusion in the report.")
