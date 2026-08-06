from sqlalchemy.orm import Session


def bulk_insert_dataframe(session: Session, model, dataframe):

    records = dataframe.to_dict(orient="records")

    session.bulk_insert_mappings(
        model,
        records,
    )

    print(f"Loaded {len(records)} rows.")