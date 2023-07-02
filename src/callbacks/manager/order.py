from aiogram import types
import models
import constants
from markups import markups
from .manager_panel import orders_destinations

order_status_text = {
    constants.OrderStatus.CREATED: constants.language.status_created,
    constants.OrderStatus.PAID: constants.language.status_paid,
    constants.OrderStatus.IN_DELIVERY: constants.language.status_in_delivery,
    constants.OrderStatus.DONE: constants.language.status_done,
}


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    message=None,
) -> None:
    order = models.orders.Order(data["oid"])
    order_status = constants.OrderStatus(await order.status)

    order_title_price = tuple(
        (item.title, item.price) for item in await order.items
    )

    text = constants.language.format_order(
        order.id,
        await order.date_created,
        await models.users.User(await order.user_id).username,
        order_status_text[order_status],
        order_title_price,
        await order.total_price,
    )

    markup = []
    if order_status.value + 1 <= 3:
        next_order_status = constants.OrderStatus(order_status.value + 1)
        markup.append(
            (
                constants.language.change_status_to(
                    order_status_text[next_order_status]
                ),
                f'{{"r":"manager","oid":{order.id},"s":{next_order_status.value}}}orders.apply_status',
            )
        )
    markup.extend(
        [
            (
                constants.language.change_status,
                f'{{"r":"manager","oid":{order.id}}}orders.change_status',
            ),
            (
                constants.language.back,
                orders_destinations[constants.OrderStatus(await order.status)],
            ),
        ]
    )

    if message:
        return await message.answer(text, reply_markup=markup)
    await callback_query.message.edit_text(
        text, reply_markup=markups.create(markup)
    )
