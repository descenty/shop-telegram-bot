from aiogram import types
import models
import constants
from markups import markups
from .orders import execute as orders_execute


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    message=None,
) -> None:
    return await orders_execute(
        callback_query,
        user,
        data | {"status": constants.OrderStatus.CREATED},
        message,
    )
