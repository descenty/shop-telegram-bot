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
    order_id = data["oid"]
    markup = [
        (
            status_text,
            f'{{"r":"manager","oid":{order_id},"s":{status}}}orders.apply_status',
        )
        for status, status_text in constants.STATUS_DICT.items()
    ]
    markup.append(
        (
            constants.language.back,
            f'{{"r":"manager","oid":{order_id}}}order',
        )
    )
    await callback_query.message.edit_reply_markup(
        reply_markup=markups.create(markup)
    )
