"""
@author gye hyun james kim <pnuskgh@gmail.com>
@copyright 2017~2025, BlueStone Inc.
@license BlueStone License 1.0
"""

import asyncio
import logging
import os
import time

from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, Request, status
from pydantic import BaseModel


def init_env() -> None:
    load_dotenv(dotenv_path=".env", override=True)

    environment: str = os.getenv("ENVIRONMENT", "development")
    load_dotenv(dotenv_path=f".env_{environment}", override=True)


def getLogger(name: str, level: int = logging.INFO) -> logging.Logger:
    logging.basicConfig(level=level)
    logger = logging.getLogger(name)
    return logger


init_env()
logger: logging.Logger = getLogger("app/mainFastAPI", logging.INFO)

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK, response_model=dict)
def read_root(request: Request) -> dict:
    client_host = request.client.host
    logger.info("Root endpoint called")
    return {"message": "Hello, FastAPI!", "client_host": client_host}


@app.get("/hello/{name}", response_model=dict)
def hello_name(
    name: str,
    skip: int = 0,
    limit: int = 10,
    user_agent: str | None = Header(default=None),
) -> dict:
    if not name.isalpha():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Name must contain only alphabetic characters",
        )
    if name.lower() == "forbidden":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden for this name",
        )
    if name.lower() == "notfound":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Name not found",
        )

    if name.lower() == "error":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred",
        )
    return {
        "message": f"Hello, {name}!",
        "skip": skip,
        "limit": limit,
        "user_agent": user_agent,
    }


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/", status_code=status.HTTP_201_CREATED, response_model=Item)
async def create_item(item: Item, request: Request) -> Item:
    start = time.time()
    body = await request.json()
    logger.info(f"Received item: {body}")

    if item.price < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price must be non-negative",
        )
    duration: int = 10
    await asyncio.sleep(duration)
    end = time.time()
    print(f"총 실행 시간: {end - start:.2f}초")
    return {"name": item.name, "price": item.price}
