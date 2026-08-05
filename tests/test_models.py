from src.models.provider import Provider
from src.models.hcpcs import HCPCSCode
from src.models.place_of_service import PlaceOfService
from src.models.provider_service_statistics import ProviderServiceStatistics

models = [
    Provider,
    HCPCSCode,
    PlaceOfService,
    ProviderServiceStatistics,
]

for model in models:
    print(f"{model.__tablename__}")

    for column in model.__table__.columns:
        print(f"  - {column.name}")

    print()