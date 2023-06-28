from aiogram import types
import models
import constants
from markups import markups
from src.models.orders import Order
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

    markup = markups.create(
        [
            (
                f"Заказ от {await order.date_created}",
                f'{{"r":"user","cid":{order.id}}}order',
            )
            for order in orders
        ]
    )

    await callback_query.message.edit_text(text=text, reply_markup=markup)
