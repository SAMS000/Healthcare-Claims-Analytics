from etl.extract import extract_data
from etl.transform import transform_providers

df = extract_data(nrows=1000)
providers = transform_providers(df)

columns = [
    "last_org_name",
    "first_name",
    "middle_initial",
    "credentials",
    "entity_code",
    "address_line1",
    "address_line2",
    "city",
    "state",
    "zip_code",
    "country",
    "provider_type",
]

for col in columns:
    print(f"\n{col}")

    lengths = (
        providers[col]
        .astype(str)
        .str.len()
    )

    print("Max length:", lengths.max())

    print(
        providers.loc[lengths.idxmax(), col]
    )