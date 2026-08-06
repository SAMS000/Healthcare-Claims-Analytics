from sqlalchemy.orm import Session

from src.models.provider import Provider
from src.models.hcpcs import HCPCSCode
from src.models.place_of_service import PlaceOfService
from src.models.provider_service_statistics import ProviderServiceStatistics

from config.database import engine
from etl.extract import extract_data
from etl.transform import transform_provider_service_statistics
from src.loaders.load import bulk_insert_dataframe
from src.models.provider_service_statistics import ProviderServiceStatistics


def main():

    print("Extracting...")
    df = extract_data(nrows=1000)

    print("Transforming...")
    statistics = transform_provider_service_statistics(df)

    session = Session(engine)

    try:

        bulk_insert_dataframe(
            session=session,
            model=ProviderServiceStatistics,
            dataframe=statistics,
        )

        session.commit()
        print("Committed!")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()