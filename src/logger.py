"""
logger.py
----------
Application Logging
"""

import logging
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "research_assistant.log")


def get_logger():

    logger = logging.getLogger("AIResearchAssistant")

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(LOG_FILE)

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger


logger = get_logger()