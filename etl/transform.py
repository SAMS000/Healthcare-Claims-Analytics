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

    providers["zip_code"] = (
        providers["zip_code"]
        .astype(str)
        .str.zfill(5)
    )

    # convert pandas NaN -> Python None
    providers = providers.astype(object).where(pd.notnull(providers), None)

    return providers
def transform_hcpcs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform HCPCS information into a normalized table.
    """

    hcpcs = (
        df[
            [
                "HCPCS_Cd",
                "HCPCS_Desc",
                "HCPCS_Drug_Ind",
            ]
        ]
        .drop_duplicates()
        .copy()
    )

    hcpcs.columns = [
        "hcpcs_code",
        "description",
        "drug_indicator",
    ]

    hcpcs["drug_indicator"] = (
        hcpcs["drug_indicator"]
        .map({"Y": True, "N": False})
    )

    return hcpcs

def transform_place_of_service(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform Place of Service information into a normalized table.
    """

    place = (
        df[
            [
                "Place_Of_Srvc",
            ]
        ]
        .drop_duplicates()
        .copy()
    )

    place.columns = [
        "place_of_service_code",
    ]

    return place

def transform_provider_service_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform provider service statistics into the fact table.
    """

    statistics = (
        df[
            [
                "Rndrng_NPI",
                "HCPCS_Cd",
                "Place_Of_Srvc",
                "Tot_Benes",
                "Tot_Srvcs",
                "Tot_Bene_Day_Srvcs",
                "Avg_Sbmtd_Chrg",
                "Avg_Mdcr_Alowd_Amt",
                "Avg_Mdcr_Pymt_Amt",
                "Avg_Mdcr_Stdzd_Amt",
            ]
        ]
        .copy()
    )

    statistics.columns = [
        "provider_npi",
        "hcpcs_code",
        "place_of_service_code",
        "total_beneficiaries",
        "total_services",
        "total_bene_day_services",
        "avg_submitted_charge",
        "avg_allowed_amount",
        "avg_payment_amount",
        "avg_standardized_amount",
    ]

    return statistics