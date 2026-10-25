# load the dataset and plot and data using line,bar,scatter plots, and heatmap with seaborn and matplotlib libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data.csv")

# Display the dataset
print("Dataset:")
print(df.head())

# Select numerical columns
num = df.select_dtypes(include="number")

# 1. Line Plot
plt.figure(figsize=(6, 4))
plt.plot(num.iloc[:, 0], marker='o')
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel(num.columns[0])
plt.show()

# 2. Bar Plot
plt.figure(figsize=(6, 4))
plt.bar(df.index[:10], num.iloc[:10, 0], color='skyblue')
plt.title("Bar Plot")
plt.xlabel("Index")
plt.ylabel(num.columns[0])
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(num.iloc[:, 0], num.iloc[:, 1], color='red')
plt.title("Scatter Plot")
plt.xlabel(num.columns[0])
plt.ylabel(num.columns[1])
plt.show()

# 4. Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(num.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()