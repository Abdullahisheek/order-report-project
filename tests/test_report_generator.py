import pandas as pd

from src.report_generator import (
    create_overview,
    create_returns_by_category,
    create_sales_report,
)


def create_test_data():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "product_category": [
                "Electronics",
                "Electronics",
                "Clothing",
            ],
            "region": [
                "Stockholm",
                "Stockholm",
                "Gothenburg",
            ],
            "discounted_value": [
                100.0,
                200.0,
                150.0,
            ],
            "returned": [
                False,
                True,
                False,
            ],
        }
    )


def test_create_overview():
    data = create_test_data()

    result = create_overview(data)

    assert result.loc[
        result["metric"] == "total_sales", "value"
    ].iloc[0] == 450.0

    assert result.loc[
        result["metric"] == "order_count", "value"
    ].iloc[0] == 3

    assert result.loc[
        result["metric"] == "return_count", "value"
    ].iloc[0] == 1


def test_create_sales_report():
    data = create_test_data()

    result = create_sales_report(
        data,
        "product_category",
    )

    electronics = result[
        result["product_category"] == "Electronics"
    ].iloc[0]

    assert electronics["order_count"] == 2
    assert electronics["total_sales"] == 300.0
    assert electronics["returns"] == 1
    assert electronics["return_rate"] == 0.5


def test_create_returns_by_category():
    data = create_test_data()

    result = create_returns_by_category(data)

    electronics = result[
        result["product_category"] == "Electronics"
    ].iloc[0]

    assert electronics["order_count"] == 2
    assert electronics["returns"] == 1
    assert electronics["return_rate"] == 0.5