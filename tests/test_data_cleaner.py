import pandas as pd

from src.data_cleaner import clean_data


def test_clean_data():
    data = pd.DataFrame(
        {
            "region": [" stockholm ", None],
            "product_category": [" electronics ", None],
            "quantity": ["2", "invalid"],
            "unit_price": ["100", "200"],
            "discount": ["0.1", None],
            "returned": ["ja", "false"],
        }
    )

    cleaned = clean_data(data)

    assert cleaned.loc[0, "region"] == "Stockholm"
    assert cleaned.loc[1, "region"] == "Unknown"

    assert cleaned.loc[0, "product_category"] == "Electronics"
    assert cleaned.loc[1, "product_category"] == "Unknown"

    assert cleaned.loc[0, "quantity"] == 2
    assert cleaned.loc[1, "quantity"] == 1

    assert cleaned.loc[0, "returned"]
    assert not cleaned.loc[1, "returned"]

    assert cleaned.loc[0, "order_value"] == 200
    assert cleaned.loc[0, "discounted_value"] == 180