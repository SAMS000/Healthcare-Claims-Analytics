from etl.extract import extract_data
from etl.transform import transform_providers

df = extract_data(nrows=1000)

providers = transform_providers(df)

print(providers.head())

print()

print(providers.shape)