import logging

from src.config import ReportConfig
from src.data_cleaner import clean_data
from src.data_loader import load_data
from src.report_generator import (
    create_overview,
    create_returns_by_category,
    create_sales_report,
)
from src.report_writer import save_report


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the order report program."""
    config = ReportConfig()

    logger.info("Startar orderrapport")

    try:
        data = load_data(config.input_file)

        logger.info("Läste in %s rader", len(data))

        data = clean_data(data)

        overview = create_overview(data)
        sales_by_category = create_sales_report(
            data,
            "product_category",
        )
        sales_by_region = create_sales_report(
            data,
            "region",
        )
        returns_by_category = create_returns_by_category(data)

        save_report(
            overview,
            config.output_folder,
            "overview.csv",
        )

        save_report(
            sales_by_category,
            config.output_folder,
            "sales_by_category.csv",
        )

        save_report(
            sales_by_region,
            config.output_folder,
            "sales_by_region.csv",
        )

        save_report(
            returns_by_category,
            config.output_folder,
            "returns_by_category.csv",
        )

        logger.info("Klart")

    except (FileNotFoundError, ValueError, OSError) as error:
        logger.error("Något gick fel: %s", error)


if __name__ == "__main__":
    main()