from aiogram import types
import models
import constants
from markups import markups
from ..order import execute as order_execute


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    message=None,
) -> None:
    order_id = data["oid"]
    status = data["s"]
    print(order_id, status)
    await models.orders.Order(order_id).set_status(status)
    await order_execute(callback_query, user, data, message)
