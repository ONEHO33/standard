"""
@author gye hyun james kim <pnuskgh@gmail.com>
@copyright 2017~2025, BlueStone Inc.
@license BlueStone License 1.0
"""

import logging

from app.calculator import add

logging.basicConfig(level=logging.INFO)


def test_add():
    logging.info("test add function")

    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
