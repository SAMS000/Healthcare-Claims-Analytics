from pathlib import Path
import pandas as pd

# Dataset path
DATA_PATH = Path("data/raw/cms_provider_service/provider_service_2025.csv")

print("=" * 60)
print("Healthcare Claims Dataset Inspection")
print("=" * 60)

# Load dataset
df = pd.read_csv(DATA_PATH)

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
for column in df.columns:
    print(f"- {column}")

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nFirst Five Rows")
print(df.head())