from aiogram import types
import models
import constants
from markups import markups
import states
import asyncio


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    message=None,
) -> None:
    text = constants.language.my_orders

    orders = await user.orders

    date_format = "%d %b. %Y %H:%M:%S"

    markup = [
        (
            f"{(await order.date_created).strftime(date_format)} - {await order.total_price} ₽",
            f'{{"r":"user","oid":{order.id}}}order',
        )
        for order in orders
    ]
    markup.append((constants.language.back, f"{constants.JSON_USER}profile"))

    await callback_query.message.edit_text(
        text=text, reply_markup=markups.create(markup)
    )
