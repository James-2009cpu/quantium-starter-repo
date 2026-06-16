import pandas as pd

import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3])

df = df[df["product"] == "Pink Morsels"]

df["Sales"] = df["quantity"] * df["price"]

output = df[["Sales", "date", "region"]]
output.columns = ["Sales", "Date", "Region"]

output.to_csv("sales_output.csv", index=False)

print("DONE")
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
