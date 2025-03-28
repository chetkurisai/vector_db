import os
import pandas as pd
import json
import re

# Define the dataset path
DATA_FOLDER = "D:/Vector_DB/Data_Sets"

# Load CSV files
sample_csv_path = os.path.join(DATA_FOLDER, "sample.csv")
twcs_csv_path = os.path.join(DATA_FOLDER, "twcs.csv")

# Load data into pandas DataFrames
sample_df = pd.read_csv(sample_csv_path)
twcs_df = pd.read_csv(twcs_csv_path)

# ✅ Step 1: Check for missing values
print("Missing values in Sample.csv:")
print(sample_df.isnull().sum())

print("\nMissing values in Twcs.csv:")
print(twcs_df.isnull().sum())

# ✅ Step 2: Drop rows with missing essential fields
sample_df.dropna(subset=["text"], inplace=True)
twcs_df.dropna(subset=["text"], inplace=True)

# ✅ Step 3: Convert timestamps to datetime format
#sample_df["created_at"] = pd.to_datetime(sample_df["created_at"], errors="coerce")
#twcs_df["created_at"] = pd.to_datetime(twcs_df["created_at"], errors="coerce")
# ✅ Step 3: Convert timestamps to datetime format with explicit format
sample_df["created_at"] = pd.to_datetime(sample_df["created_at"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
twcs_df["created_at"] = pd.to_datetime(twcs_df["created_at"], format="%Y-%m-%d %H:%M:%S", errors="coerce")



# ✅ Step 4: Standardize text (remove URLs, special characters, and lowercasing)
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text.lower().strip()

sample_df["text"] = sample_df["text"].astype(str).apply(clean_text)
twcs_df["text"] = twcs_df["text"].astype(str).apply(clean_text)

# ✅ Step 5: Save the cleaned data to JSON files
sample_df.to_json(os.path.join(DATA_FOLDER, "sample_cleaned.json"), orient="records", lines=True)
twcs_df.to_json(os.path.join(DATA_FOLDER, "twcs_cleaned.json"), orient="records", lines=True)

print("\n✅ Data preprocessing complete! Cleaned data saved.")
