from datetime import datetime
import json
from aiogram import types
from aiogram.dispatcher import FSMContext
import models
import constants
from markups import markups

import states

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
    checkout_settings = constants.config["checkout"]
    text = constants.language.unknown_error

    markup = [(constants.language.back, f'{{"r":"user","d":"cart"}}cancel')]
    if checkout_settings["email"]:
        text = constants.language.input_email
        await states.Order.email.set()
    elif checkout_settings["phone"]:
        text = constants.language.input_phone
        await states.Order.phone_number.set()
    elif checkout_settings["address"]:
        text = constants.language.input_address
        await states.Order.address.set()
    elif checkout_settings["captcha"]:
        text = constants.language.input_captcha
        markup = [
            (constants.language.refresh, f'{{"r":"user"}}refresh')
        ] + markup
        await states.Order.captcha.set()
    else:
        # text = constants.language.input_comment
        # await states.Order.comment.set()

        # await callback_query.message.edit_text(
        # text=text, reply_markup=markups.create(markup)
        # )

        # await states.Order.confirmation.set()
        order_items_amount = [
            (models.items.Item(int(item_id)), amount)
            for item_id, amount in (await user.cart.items.dict).items()
        ]
        cart_items_dict = [
            {
                "id": item.id,
                "title": await item.name,
                "amount": amount,
                "price": await item.price,
            }
            for item, amount in order_items_amount
        ]
        cart_items = json.dumps(cart_items_dict)

        await user.cart.items.clear()

        order = await models.orders.create(
            user_id=user.id, items_json=cart_items
        )

        await callback_query.message.edit_text(
            text=constants.language.confirm_order,
            reply_markup=markups.create([]),
        )

        # notify all managers

        managers = await models.users.get_managers()

        order_status = constants.OrderStatus(await order.status)

        order_title_price = tuple(
            (item.title, item.price) for item in await order.items
        )

        text = constants.language.new_order + "\n"

        text += constants.language.format_order(
            order.id,
            await order.date_created,
            await user.username,
            order_status_text[order_status],
            order_title_price,
            await order.total_price,
        )

        for manager in managers:
            await constants.bot.send_message(manager.id, text)
