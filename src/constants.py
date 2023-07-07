from enum import Enum
import importlib

import aiogram
from config import config
import os
import asyncio

if not os.path.exists("config.json"):
    config.init()

import localization.ru as language

# language = importlib.import_module(f"localization.{config['settings']['language']}")

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class OrderStatus(Enum):
    CREATED = 0
    PAID = 1
    IN_DELIVERY = 2
    DONE = 3
    CANCELED = -1


STATUS_DICT = {
    0: language.status_created,
    1: language.status_paid,
    2: language.status_in_delivery,
    3: language.status_done,
    -1: language.status_canceled,
}

JSON_USER = '{"r": "user"}'
JSON_MANAGER = '{"r": "manager"}'
JSON_ADMIN = '{"r": "admin"}'

loop = asyncio.new_event_loop()

bot = None


def create_bot(token: str) -> aiogram.bot.bot.Bot:
    global bot
    # api_server = aiogram.bot.api.TelegramAPIServer(
    #     "https://api.bots.mn/telegram/", "https://api.bots.mn/telegram/"
    # )
    bot = aiogram.Bot(token=token, loop=loop, proxy="https://api.bots.mn/telegram/")
    return bot
