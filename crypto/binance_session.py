import os
from binance import Client


def connect_API() -> Client:
    key = os.environ.get("APIKEY")
    secret = os.environ.get("APISECRET")
    return Client(key, secret)
