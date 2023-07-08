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
    orders_statuses_dates = zip(
        orders,
        [await order.status for order in await user.orders],
        [await order.date_created for order in await user.orders],
    )
    orders_statuses_dates = sorted(
        orders_statuses_dates, key=lambda x: (x[1], x[2])
    )

    date_format = "%d %b. %Y %H:%M:%S"
    # TODO client order view
    markup = [
        (
            f"{(date).strftime(date_format)} - {await order.total_price} ₽ {constants.STATUS_DICT[status]}",
            f'{{"r":"user","oid":{order.id}}}order',
        )
        for order, status, date in orders_statuses_dates
        if constants.OrderStatus(status)
        not in [constants.OrderStatus.DONE, constants.OrderStatus.CANCELED]
    ]
    markup.append((constants.language.back, f"{constants.JSON_USER}profile"))

    if message:
        return await message.answer(
            text=text, reply_markup=markups.create(markup)
        )
    await callback_query.message.edit_text(
        text=text, reply_markup=markups.create(markup)
    )
