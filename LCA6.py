import pandas as pd

# Read the file
file = input("Enter file name (.csv/.xls/.xlsx): ")

if file.endswith(".csv"):
    df = pd.read_csv(file)
elif file.endswith((".xls", ".xlsx")):
    df = pd.read_excel(file)
else:
    print("Invalid file format")
    exit()

# Display original data
print("\nOriginal Data:")
print(df)

# Display missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")
    else:
        df[col] = df[col].fillna(df[col].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Display cleaned data
print("\nPreprocessed Data:")
print(df)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned data saved to cleaned_data.csv")
