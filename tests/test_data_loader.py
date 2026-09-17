import pandas as pd
import pytest

from src.data_loader import load_data, validate_columns


def test_load_data():
    data = load_data("data/orders.csv")

    assert isinstance(data, pd.DataFrame)
    assert len(data) == 80


def test_validate_columns_missing_column():
    data = pd.DataFrame(
        {
            "order_id": [1],
            "region": ["Stockholm"],
        }
    )

    with pytest.raises(ValueError):
        validate_columns(data)

def test_load_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_data("data/does_not_exist.csv")