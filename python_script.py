import pandas as pd

# Load dataset
df = pd.read_csv("online_retail.csv")

print("Original shape:", df.shape)

# Show column names
print("Columns in dataset:")
print(df.columns)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create new column: Total Sales
df["Total Sales"] = df["List Price"] * df["Quantity"]

# Create Year column
df["Year"] = df["Order Date"].dt.year

# Create Month column
df["Month"] = df["Order Date"].dt.month

# Remove negative values if any
df = df[df["Quantity"] > 0]
df = df[df["List Price"] > 0]

print("Cleaned shape:", df.shape)

# Save cleaned dataset
df.to_csv("cleaned_online_retail.csv", index=False)

print("Cleaning completed successfully.")