import pandas as pd


def create_overview(data: pd.DataFrame) -> pd.DataFrame:
    """Create an overview of sales, orders and returns."""
    total_sales = round(
        data["discounted_value"].sum(),
        2,
    )

    number_of_orders = data["order_id"].nunique()
    number_of_returns = int(data["returned"].sum())

    return pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )


def create_sales_report(
    data: pd.DataFrame,
    group_by: str,
) -> pd.DataFrame:
    """Create a sales report grouped by a selected column."""
    result = (
        data.groupby(
            group_by,
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    result["total_sales"] = result["total_sales"].round(2)

    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    return (
        result
        .sort_values(
            "total_sales",
            ascending=False,
        )
        .reset_index(drop=True)
    )


def create_returns_by_category(
    data: pd.DataFrame,
) -> pd.DataFrame:
    """Create a return report grouped by product category."""
    result = (
        data.groupby(
            "product_category",
            as_index=False,
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    result["return_rate"] = (
        result["returns"] / result["order_count"]
    ).round(3)

    return (
        result
        .sort_values(
            "return_rate",
            ascending=False,
        )
        .reset_index(drop=True)
    )