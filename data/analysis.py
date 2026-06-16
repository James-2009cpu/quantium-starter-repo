import pandas as pd

# Load all CSV files
df1 = pd.read_csv("data/file1.csv")
df2 = pd.read_csv("data/file2.csv")
df3 = pd.read_csv("data/file3.csv")

# Combine them
df = pd.concat([df1, df2, df3])

# Keep only Pink Morsels
df = df[df["product"] == "Pink Morsels"]

# Create sales column
df["Sales"] = df["quantity"] * df["price"]

# Keep only required columns
output = df[["Sales", "date", "region"]]

# Rename to match spec exactly
output.columns = ["Sales", "Date", "Region"]

# Save output file
output.to_csv("sales_output.csv", index=False)

print("Done - file created: sales_output.csv")
