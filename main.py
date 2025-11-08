"""
@author gye hyun james kim <pnuskgh@gmail.com>
@copyright 2017~2025, BlueStone Inc.
@license BlueStone License 1.0
"""

import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

environment: str = os.getenv("ENVIRONMENT", "development")
load_dotenv(dotenv_path=f".env_{environment}", override=True)


def main():
    debug: bool = os.getenv("DEBUG", "False") == "True"
    if debug:
        print("Debugging is enabled")
    print("Hello from standard!")


if __name__ == "__main__":
    main()
