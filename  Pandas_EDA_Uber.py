import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (ensure this file is in your folder)
df = pd.read_csv("Uber Request Data.csv")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Show column names
print("\nColumn Names:")
print(df.columns)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill or drop missing values
df['Pickup point'] = df['Pickup point'].fillna('Unknown')
df = df.dropna(subset=['Drop timestamp'])  # Drop if drop time is missing

# Convert time columns to datetime
df['Request timestamp'] = pd.to_datetime(df['Request timestamp'], errors='coerce')
df['Drop timestamp'] = pd.to_datetime(df['Drop timestamp'], errors='coerce')

# Create hour and daypart columns
df['hour'] = df['Request timestamp'].dt.hour
df['daypart'] = pd.cut(
    df['hour'],
    bins=[0, 4, 8, 12, 16, 20, 24],
    labels=['Late Night', 'Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night'],
    right=False
)

# Plot: Trip Status Distribution
plt.figure(figsize=(6,4))
df['Status'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Trip Status Distribution")
plt.ylabel("Number of Requests")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("status_distribution.png")
plt.close()

# Plot: Hourly Requests by Status
plt.figure(figsize=(10,6))
sns.countplot(x='hour', hue='Status', data=df)
plt.title("Hourly Requests by Status")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("hourly_status.png")
plt.close()

# Plot: Pickup Point vs Status
pickup_status = pd.crosstab(df['Pickup point'], df['Status'], normalize='index')
pickup_status.plot(kind='bar', stacked=True, figsize=(6,4))
plt.title("Pickup Point vs Status")
plt.ylabel("Proportion")
plt.tight_layout()
plt.savefig("pickup_status.png")
plt.close()

print("\n✅ EDA complete. Charts saved as:")
print("• status_distribution.png")
print("• hourly_status.png")
print("• pickup_status.png")
