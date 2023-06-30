from aiogram import types
import models
import constants
from markups import markups

orders_destinations = {
    constants.OrderStatus.CREATED: f"{constants.JSON_MANAGER}orders.created_orders",
    constants.OrderStatus.PAID: f"{constants.JSON_MANAGER}orders.paid_orders",
    constants.OrderStatus.IN_DELIVERY: f"{constants.JSON_MANAGER}orders.in_delivery_orders",
    constants.OrderStatus.DONE: f"{constants.JSON_MANAGER}orders.done_orders",
}


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    message=None,
) -> None:
    text = constants.language.manager_panel
    markup = markups.create(
        [
            (
                constants.language.created_orders_short,
                orders_destinations[constants.OrderStatus.CREATED],
            ),
            (
                constants.language.paid_orders_short,
                orders_destinations[constants.OrderStatus.PAID],
            ),
            (
                constants.language.in_delivery_orders_short,
                orders_destinations[constants.OrderStatus.IN_DELIVERY],
            ),
            (
                constants.language.done_orders_short,
                orders_destinations[constants.OrderStatus.DONE],
            ),
        ]
    )

    if message:
        return await message.answer(text, reply_markup=markup)
    await callback_query.message.edit_text(text, reply_markup=markup)
