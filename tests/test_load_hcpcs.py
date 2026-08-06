from sqlalchemy.orm import Session

from config.database import engine
from etl.extract import extract_data
from etl.transform import transform_hcpcs
from src.loaders.load import bulk_insert_dataframe
from src.models.hcpcs import HCPCSCode


def main():

    print("Extracting...")
    df = extract_data(nrows=1000)

    print("Transforming...")
    hcpcs = transform_hcpcs(df)

    session = Session(engine)

    try:

        bulk_insert_dataframe(
            session=session,
            model=HCPCSCode,
            dataframe=hcpcs,
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