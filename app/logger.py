import logging
import os


def configure_logger():
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("portfolio_app")

    # Prevent duplicate handlers
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Write logs to a file
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(formatter)

    # Show logs in the terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger