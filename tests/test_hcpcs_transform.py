from etl.extract import extract_data
from etl.transform import transform_hcpcs

df = extract_data(nrows=1000)

hcpcs = transform_hcpcs(df)

print(hcpcs.head())

print()

print(hcpcs.shape)