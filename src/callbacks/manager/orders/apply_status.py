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
    order = models.orders.Order(order_id)
    await order.set_status(status)
    await order_execute(callback_query, user, data, message)
    await constants.bot.send_message(await order.user_id, constants.language.order_status_changed(order_id, constants.STATUS_DICT[status]))
    
