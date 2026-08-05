from etl.extract import extract_data
from etl.transform import transform_provider_service_statistics

print("Loading dataset...")

df = extract_data()

print("Transforming statistics...")

statistics = transform_provider_service_statistics(df)

print()

duplicates = statistics.duplicated(
    subset=[
        "provider_npi",
        "hcpcs_code",
        "place_of_service_code",
    ]
).sum()

print(f"Duplicate composite keys: {duplicates}")