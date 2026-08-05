from etl.extract import extract_data
from etl.transform import transform_provider_service_statistics

df = extract_data(nrows=1000)

statistics = transform_provider_service_statistics(df)

print(statistics.head())

print()

print(statistics.shape)