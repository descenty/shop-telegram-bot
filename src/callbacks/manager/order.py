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

    next_order_status = constants.OrderStatus(order_status.value + 1)

    date_format = "%d %b. %Y %H:%M:%S"
    text_list = [
        f"Заказ №{order.id} от {(await order.date_created).strftime(date_format)}",
        f"Telegram: @{await models.users.User(await order.user_id).username}",
        f"Статус: {order_status_text[order_status]}",
        "---",
    ]
    text_list.extend(
        [
            f"{index + 1}. {item.title} - {item.price} ₽"
            for index, item in enumerate(await order.items)
        ]
    )
    text_list.extend(["---", f"Итого: {await order.total_price} ₽"])
    text = "\n".join(text_list)
    markup = markups.create(
        [
            (
                constants.language.change_status_to(
                    order_status_text[next_order_status]
                ),
                f'{{"r":"manager","oid":{order.id},"s":{next_order_status}}}orders.apply_status',
            ),
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
    await callback_query.message.edit_text(text, reply_markup=markup)
