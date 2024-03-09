import pathlib
import os
from typing import Final
from pymongo import MongoClient
from dotenv import load_dotenv
import logging
from logging.config import dictConfig


load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# Database for Inventory
SQL_PASSWORD: Final[str] = os.getenv("SQL_PASSWORD")

# Imgur API
IMGUR_ID: Final[str] = os.getenv("IMGUR_CLIENT_ID")
IMGUR_SECRET: Final[str] = os.getenv("IMGUR_CLIENT_SECRET")

# Directories
BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"

# API Clients #
YOUTUBE_KEY: Final[str] = os.getenv("YOUTUBE_API_KEY")

# MongoDB
MONGODB_NAME: Final[str] = os.getenv("MONGODB_NAME")
MONGODB_URL: Final[str] = os.getenv("MONGODB_URL")

mongodb = MongoClient(MONGODB_URL)
collection = mongodb[MONGODB_NAME]["Settings"]
playlist = mongodb[MONGODB_NAME]["Playlist"]


# Logging
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {"format": "%(levelname)-10s - %(name)-15s : %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "./logs/info.log",
            "mode": "w",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "bot": {"handlers": ["console"], "level": "INFO", "propagate": False},
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
