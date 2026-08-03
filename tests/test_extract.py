from etl.extract import extract_data

df = extract_data(nrows=5)

print(df.head())
print()
print(df.shape)