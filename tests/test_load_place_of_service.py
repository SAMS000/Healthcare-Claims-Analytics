from sqlalchemy.orm import Session

from config.database import engine
from etl.extract import extract_data
from etl.transform import transform_place_of_service
from src.loaders.load import bulk_insert_dataframe
from src.models.place_of_service import PlaceOfService


def main():

    print("Extracting...")
    df = extract_data(nrows=1000)

    print("Transforming...")
    pos = transform_place_of_service(df)

    session = Session(engine)

    try:

        bulk_insert_dataframe(
            session=session,
            model=PlaceOfService,
            dataframe=pos,
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