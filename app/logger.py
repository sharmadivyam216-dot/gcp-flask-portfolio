import logging
import os


def configure_logger():
    logger = logging.getLogger("portfolio_app")

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Console logging (works locally and on Google Cloud)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Only create log files when running locally
    if not os.getenv("GAE_ENV"):
        os.makedirs("logs", exist_ok=True)

        file_handler = logging.FileHandler("logs/app.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger