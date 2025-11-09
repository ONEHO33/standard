"""
@author gye hyun james kim <pnuskgh@gmail.com>
@copyright 2017~2025, BlueStone Inc.
@license BlueStone License 1.0
"""

import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI


def init_env() -> None:
    load_dotenv(dotenv_path=".env", override=True)

    environment: str = os.getenv("ENVIRONMENT", "development")
    load_dotenv(dotenv_path=f".env_{environment}", override=True)


def getLogger(level: int, name: str) -> logging.Logger:
    logging.basicConfig(level=level)
    logger = logging.getLogger(name)
    return logger


init_env()
logger: logging.Logger = getLogger(logging.INFO, "app/main")

app = FastAPI()


@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Hello, FastAPI!"}
