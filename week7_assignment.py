# ==============================================================
# Assignment: Data Loading, Analysis, and Visualization
# ==============================================================

# -------------------------------
# Step 0: Import Libraries
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set_style("whitegrid")

# -------------------------------
# Task 1: Load and Explore Dataset
# -------------------------------
try:
    # Load Iris dataset from seaborn (you can also use pd.read_csv('your_dataset.csv'))
    df = pd.read_csv('iris.csv')
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Explore dataset info and missing values
print("Dataset Info:")
print(df.info(), "\n")
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# Drop missing values if any
df_clean = df.dropna()
print("Dataset after cleaning:")
print(df_clean.info(), "\n")

# -------------------------------
# Task 2: Basic Data Analysis
# -------------------------------
# Basic statistics of numerical columns
print("Basic statistics of numerical columns:")
print(df_clean.describe(), "\n")

# Group by species and calculate mean
grouped = df_clean.groupby('species').mean()
print("Mean values by species:")
print(grouped, "\n")

# Observations
print("Observations:")
print("- Setosa generally has smaller sepal and petal measurements.")
print("- Virginica tends to have larger sepal and petal measurements.")
print("- Versicolor is intermediate between Setosa and Virginica.\n")

# -------------------------------
# Task 3: Data Visualization
# -------------------------------

# 1. Line Chart: Sepal Length Trend
plt.figure(figsize=(8,5))
plt.plot(df_clean['sepal_length'], label='Sepal Length', marker='o')
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8,5))
grouped['petal_length'].plot(kind='bar', color=['skyblue','lightgreen','salmon'])
plt.title("Bar Chart: Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: Sepal Width Distribution
plt.figure(figsize=(8,5))
plt.hist(df_clean['sepal_width'], bins=10, color='lightcoral', edgecolor='black')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,5))
sns.scatterplot(data=df_clean, x='sepal_length', y='petal_length', hue='species', s=100)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# -------------------------------
# Conclusion
# -------------------------------
print("Analysis complete. Key observations:")
print("- Setosa has the smallest measurements, Virginica the largest.")
print("- Versicolor is intermediate in size.")
print("- Plots show trends, distributions, and relationships clearly.")