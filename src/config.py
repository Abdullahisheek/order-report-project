from dataclasses import dataclass


@dataclass
class ReportConfig:
    """Configuration for the order report."""

    input_file: str = "data/orders.csv"
    output_folder: str = "output"