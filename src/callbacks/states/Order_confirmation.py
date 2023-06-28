from aiogram import types
from aiogram.dispatcher import FSMContext
import models.orders
import constants
from markups import markups
from datetime import datetime
import json


async def execute(
    callback_query: types.CallbackQuery,
    user: models.users.User,
    data: dict,
    state: FSMContext,
    message: types.Message = None,
) -> None:
    # call = callback_query.data[callback_query.data.index("}")+1:]

    # await state.update_data()
    # state_data = await state.get_data()

    cart_items = json.dumps(await user.cart.items.dict)
    
    await user.cart.items.clear()

    await models.orders.create(user_id=user.id, items_json=cart_items, date_created=datetime.now())

    await callback_query.message.edit_text(
        text=constants.language.confirm_order, reply_markup=markups.create([])
    )
    await state.finish()
