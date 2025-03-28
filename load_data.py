import pandas as pd
import os

# Define the dataset path
DATA_FOLDER = "D:/Vector_DB/Data_Sets"

# Load CSV files
sample_path = os.path.join(DATA_FOLDER, "sample.csv")
twcs_path = os.path.join(DATA_FOLDER, "twcs.csv")

# Read CSV files into Pandas DataFrames
sample_df = pd.read_csv(sample_path)
twcs_df = pd.read_csv(twcs_path, nrows=10000)  # Load only 10,000 rows for testing

# Display basic info
print("Sample.csv Info:")
print(sample_df.info())
print("\nSample.csv Head:")
print(sample_df.head())

print("\nTwcs.csv Info (First 10,000 rows only):")
print(twcs_df.info())
print("\nTwcs.csv Head:")
print(twcs_df.head())

# Save as JSON (for further processing)
sample_df.to_json(os.path.join(DATA_FOLDER, "sample.json"), orient="records", lines=True)
twcs_df.to_json(os.path.join(DATA_FOLDER, "twcs_sample.json"), orient="records", lines=True)

print("\n✅ Data loaded and saved as JSON (sample only)!")
