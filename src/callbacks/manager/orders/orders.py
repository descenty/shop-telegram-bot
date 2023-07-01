from aiogram import types
import models
import constants
from markups import markups
from models.users import User
import states
import asyncio

orders_text_dict = {
    constants.OrderStatus.CREATED: constants.language.created_orders,
    constants.OrderStatus.PAID: constants.language.paid_orders,
    constants.OrderStatus.IN_DELIVERY: constants.language.in_delivery_orders,
    constants.OrderStatus.DONE: constants.language.done_orders,
}


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    message=None,
) -> None:
    text = orders_text_dict[data["s"]]

    orders = await models.orders.get_orders_by_status(data["s"].value)
    
    date_format = "%d %b. %Y %H:%M:%S"
    
    markup = [
        (
            f"{(await order.date_created).strftime(date_format)} - {await order.total_price} ₽",
            f'{{"r":"manager","oid":{order.id}}}order',
        )
        for order in orders
    ]
    markup.append(
        (constants.language.back, f"{constants.JSON_MANAGER}manager_panel")
    )

    await callback_query.message.edit_text(
        text=text, reply_markup=markups.create(markup)
    )
