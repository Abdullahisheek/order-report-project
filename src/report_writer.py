import logging
import os

import pandas as pd


logger = logging.getLogger(__name__)


def save_report(
    report: pd.DataFrame,
    output_folder: str,
    filename: str,
) -> None:
    """Save a report as a CSV file."""
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(
        output_folder,
        filename,
    )

    try:
        report.to_csv(
            output_path,
            index=False,
        )
    except OSError as error:
        logger.error(
            "Kunde inte spara rapporten %s: %s",
            filename,
            error,
        )
        raise

    logger.info("Sparade %s", filename)