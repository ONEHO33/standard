"""
@author gye hyun james kim <pnuskgh@gmail.com>
@copyright 2017~2025, BlueStone Inc.
@license BlueStone License 1.0
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app/calculator")


def add(a: int, b: int) -> int:
    logging.info(f"Adding {a} and {b}")
    logger.info(f"Adding {a} and {b}")
    return a + b
