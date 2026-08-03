from pathlib import Path

import pandas as pd

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset directory
DATA_DIR = PROJECT_ROOT / "data" / "raw" / "cms_provider_service"


def get_dataset_path() -> Path:
    """
    Automatically locate the CMS provider-service CSV.
    """

    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV file found in:\n{DATA_DIR}"
        )

    return csv_files[0]


def extract_data(nrows=None) -> pd.DataFrame:
    """
    Extract CMS Provider & Service dataset.
    """

    dataset_path = get_dataset_path()

    return pd.read_csv(
        dataset_path,
        low_memory=False,
        nrows=nrows,
    )