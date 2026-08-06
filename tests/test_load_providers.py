from sqlalchemy.orm import Session

from config.database import engine
from etl.extract import extract_data
from etl.transform import transform_providers
from src.loaders.load import bulk_insert_dataframe
from src.models.provider import Provider


def main():

    print("Extracting...")
    df = extract_data(nrows=1000)

    print("Transforming...")
    providers = transform_providers(df)

    #print("\nData types:")
    #print(providers.dtypes)

    print("\nConnecting to database...")
    session = Session(engine)

    try:

        bulk_insert_dataframe(
            session=session,
            model=Provider,
            dataframe=providers,
        )

        session.commit()
        print("Committed!")

    except Exception as e:

        session.rollback()
        print("Transaction rolled back.")
        raise e

    finally:

        session.close()


if __name__ == "__main__":
    main()