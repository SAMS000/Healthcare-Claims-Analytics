from etl.extract import extract_data
from etl.transform import transform_place_of_service

df = extract_data(nrows=1000)

place = transform_place_of_service(df)

print(place)

print()

print(place.shape)