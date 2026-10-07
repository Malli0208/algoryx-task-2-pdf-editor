import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"


def setup_logging():
    """Configure application logging."""

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    logging.info("PDF Editor application started.")


def log_error(error):
    """Log an application error."""
    logging.error("Error: %s", error)


def log_info(message):
    """Log an informational message."""
    logging.info(message)