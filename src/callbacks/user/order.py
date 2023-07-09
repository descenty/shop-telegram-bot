from aiogram import types
import models
import constants
from markups import markups

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

    manager = (await models.users.get_managers())[
        0
    ]  # в идеале для каждого заказа назначать своего менеджера или отображать всех менеджеров

    text = constants.language.format_user_order(
        order.id,
        await order.date_created,
        await manager.username,
        order_status_text[order_status],
        order_title_price,
        await order.total_price,
    )

    markup = [
        (
            constants.language.back,
            f"{constants.JSON_USER}orders",
        )
    ]

    if message:
        return await message.answer(text, reply_markup=markup)
    await callback_query.message.edit_text(
        text, reply_markup=markups.create(markup)
    )
