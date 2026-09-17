import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}


def load_data(file_path: str) -> pd.DataFrame:
    """Read order data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"CSV-filen kunde inte hittas: {file_path}"
        ) from error

    validate_columns(data)

    return data


def validate_columns(data: pd.DataFrame) -> None:
    """Check that all required columns exist."""
    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(
            f"Följande obligatoriska kolumner saknas: {missing}"
        )