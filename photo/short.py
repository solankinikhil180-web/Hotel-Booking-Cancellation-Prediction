import pandas as pd

# Read original CSV
df = pd.read_csv("old_data.csv")

# Remove records where number of weekend nights is 0
df = df[df["number of weekend nights"] != "0"]

# Save remaining records to a new CSV
df.to_csv("new_data.csv", index=False)

print("Done! Data saved to new_data.csv")