import pandas as pd


def transform_providers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform provider information into a normalized table.
    """

    providers = (
        df[
            [
                "Rndrng_NPI",
                "Rndrng_Prvdr_Last_Org_Name",
                "Rndrng_Prvdr_First_Name",
                "Rndrng_Prvdr_MI",
                "Rndrng_Prvdr_Crdntls",
                "Rndrng_Prvdr_Ent_Cd",
                "Rndrng_Prvdr_St1",
                "Rndrng_Prvdr_St2",
                "Rndrng_Prvdr_City",
                "Rndrng_Prvdr_State_Abrvtn",
                "Rndrng_Prvdr_Zip5",
                "Rndrng_Prvdr_Cntry",
                "Rndrng_Prvdr_Type",
                "Rndrng_Prvdr_Mdcr_Prtcptg_Ind",
            ]
        ]
        .drop_duplicates()
        .copy()
    )

    providers.columns = [
        "npi",
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
        "medicare_participating",
    ]

    providers["medicare_participating"] = (
        providers["medicare_participating"]
        .map({"Y": True, "N": False})
    )

    return providers