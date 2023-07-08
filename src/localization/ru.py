from datetime import datetime

# Misc buttons
try_again = "Попробуйте ещё раз."
skip = "⏭ Пропустить"
back = "🔙 Назад"
skip = "⏭ Пропустить"
tick = "✅"
cross = "❌"
yes = "✅ Да"
no = "❌ Нет"
enabled = "✅ Включено"
disabled = "❌ Выключено"
error = "Произошла ошибка!"
or_press_back = 'или нажмите на кнопку "Назад".'
or_press_skip = 'или нажмите на кнопку "Пропустить".'
hide = "🙈 Скрыть"
show = "🐵 Показать"
delete = "❌ Удалить"
reset = "❌ Сбросить"
no_permission = "У вас нет прав для выполнения данной команды!"
unknown_command = "Не могу понять команду :("
cross = "❌"
too_many_categories = "Слишком много категорий!"
unknown_call_stop_state = "Бот ожидает от вас ввода данных, но вы ничего не ввели. Для выхода из режима ввода данных нажмите на кнопку ниже."
state_cancelled = "Вы отменили операцию."
unknown_error = "Произошла неизвестная ошибка!"

# main markup
admin_panel = "🔴 Админ панель"
faq = "ℹ️ FAQ"
profile = "📁 Профиль"
catalogue = "🗄️ Каталог"
cart = "🛒 Корзина"
support_menu = "☎ Меню тех. поддержки"

# Cart
payment_method = "💳 Способ оплаты"
choose_payment_method = "Выберите способ оплаты:"


def format_delivery(delivery_price: int) -> str:
    return f"🚚 Доставка: {delivery_price} руб."


delivery = "🚚 Доставка"
self_pickup = "🖐️ Самовывоз"
cart_empty = "Корзина пуста."


def cart_total_price(price: float, currency_sym: str) -> str:
    return f"🛒 Итого: {price:.2f} {currency_sym}"


# Admin panel tabs
item_management = "📦 Управление товаром"
no_categories = "Создайте хотя бы одну категорию перед созданием товара!"
user_management = "🧍 Управление пользователями"
category_management = "📁 Категории"
stats = "📈 Статистика"
settings = "⚙ Настройки"

# Main settings
language = "🌐 Язык"
choose_a_language = f"Выберите язык {or_press_skip}:"
language_was_set = (
    "Язык был успешно изменен! Для применения изменений перезапустите бота."
)
english = "🇬🇧 Английский"
russian = "🇷🇺 Русский"
input_greeting = 'Форматирование: \n"%s" - ник пользователя\n\nВведите приветственное сообщение:'
greeting_was_set = "Приветственное сообщение было успешно изменено!"

greeting = "👋 Приветствие"

# FAQ
contacts = "📞 Контакты"
refund_policy = "🎫 Политика возврата"

# Profile
my_orders = "📦 Мои заказы"
cancel_order = "❌ Отменить заказ"
restore_order = "✅ Восстановить заказ"
my_support_tickets = "🙋 Мои тикеты в тех. поддержку"
enable_notif = "🔔Включить оповещения о заказах"
disable_notif = "🔕Выключить оповещения о заказах"

# Catalogue / Item / Cart
search = "🔍 Найти"
add_to_cart = "🛒 Добавить в корзину"
not_in_stock = "❌ Нет в наличии"
cart_is_empty = "Корзина пуста."
category_is_empty = "Категория пуста."
textpickup = "✅ Самовывоз"


def delivery_on(price):
    return f"✅ Доставка - {price}руб."


def delivery_off(price):
    return f"❌ Доставка - {price}руб."


cart_checkout = "Оформить заказ"
clear_cart = "Очистить корзину"


def choose_new_status(order_id: int):
    return f"Выберите новый статус заказа № {order_id}:"


change_status = "Изменить статус"


def change_status_to(new_status):
    return f"Изменить статус на {new_status}"


def order_status_changed(order_id: int, new_status: str):
    return f"Статус заказа № {order_id} был изменен на {new_status}"


new_order = "Новый заказ!"


def format_order(
    order_id: int,
    date_created: datetime,
    username: str,
    status_text: str,
    title_price: tuple[tuple[str, int]],
    total_price: float,
) -> str:
    date_format = "%d %b. %Y %H:%M:%S"
    text_list = [
        f"Заказ № {order_id} от {(date_created).strftime(date_format)}",
        f"Telegram: @{username}",
        f"Статус: {status_text}",
        "---",
    ]
    text_list.extend(
        [
            f"{index + 1}. {title} - {price} ₽"
            for index, (title, price) in enumerate(title_price)
        ]
    )
    text_list.extend(["---", f"Итого: {total_price} ₽"])
    return "\n".join(text_list)


status_created = "📝 Создан"
created_orders_short = "📝 Созданные"
created_orders = "📝 Созданные заказы"

status_paid = "💰 Оплачен"
paid_orders_short = "💰 Оплаченные"
paid_orders = "💰 Оплаченные заказы"

status_in_delivery = "🚚 В доставке"
in_delivery_orders_short = "🚚 В доставке"
in_delivery_orders = "🚚 Заказы в доставке"

status_done = "✅ Завершен"
done_orders_short = "✅ Завершенные"
done_orders = "✅ Завершенные заказы"

status_canceled = "❌ Отменен"
canceled_orders = "❌ Отмененные заказы"


def item(item):
    stock = "под заказ" if item.is_custom else f"{item.amount}"
    return f"{item.name}\n{item.price:.2f} руб.\nВ наличии: {stock}\n{item.description}"


# Category management
add_category = "🛍️ Добавить категорию"
edit_category = "✏️ Редактировать категорию"
input_category_name = f"Введите название категории {or_press_back}"
set_parent_category = f"📁 Выберите родительскую категорию {or_press_skip}"
category_created = "Категория успешно создана."


def format_category(
    category_id, category_name, category_parent_id, category_parent_name
):
    return f"Категория: [{category_id}]{category_name}\nРодительская категория: {f'[{category_parent_id}]{category_parent_name}' if category_parent_id else 'Нет'}"


edit_parent_category = "📁 Изменить родительскую категорию"
choose_a_category_to_edit = "Выберите категорию для редактирования:"
confirm_delete_category = "Вы уверены, что хотите удалить категорию?"
category_deleted = "Категория успешно удалена."


# Item management
def format_editItemsCategory_text(category_name: str) -> str:
    return f"Выберите товар для редактирования в категории {category_name}:"


add_item = "🗃️ Добавить товар"
edit_item = "✏️ Редактировать товар"

edit_name = "📋 Изменить название"
input_item_name = f"Введите название товара {or_press_back}"

choose_category = "📁 Выберите категорию"
select_item_category = f"📁 Выберите категорию товара {or_press_back}"
edit_category = "✏️ Изменить категорию"

input_item_description = f"Введите описание товара {or_press_back}"
edit_description = "📝 Изменить описание"

input_item_price = f"Введите цену товара {or_press_back}"
edit_price = "💰 Изменить цену"
price_must_be_number = "Цена должна быть числом."

send_item_images = f"🖼️ Отправьте изображение товара {or_press_skip}"
send_item_changed_images = f"🖼️ Отправьте изображение товара {or_press_back}"
delete_image = "❌ Удалить изображение"
edit_image = "🖼️ Изменить изображение"


confirm_delete_item = "Вы уверены, что хотите удалить товар?"
item_was_deleted = "Товар успешно удален."
change_desc = "📝 Изменить описание"
change_price = "🏷️ Изменить цену"
change_item_cat = "🛍️ Изменить категорию"
change_stock = "📦 Изменить кол-во"


def format_confirm_item(
    name: str,
    description: str,
    category_id: int,
    price: float,
    images: list[str],
) -> str:
    return f"Товар: {name}\nОписание: {description}\nКатегория: {category_id}\nЦена: {price}\nId изображения: {images}\n\nВы уверены, что хотите создать товар?"


item_added = "Товар успешно добавлен."

# User management
user_does_not_exist = "Пользователь не найден. {try_again}"


def format_user_profile(
    id: int,
    username: str,
    registration_date: str,
    is_admin: bool,
    is_manager: bool,
) -> str:
    role = "Пользователь"
    if is_admin:
        role = "Администратор"
    elif is_manager:
        role = "Менеджер"
    return f"ID: {id}\nИмя: {username}\nДата регистрации: {registration_date}\nРоль: {role}"


invalid_user_id = "Неверный ID пользователя. {try_again}"

user_profile = "📁Профиль пользователя"
input_user_id = f"Введите ID пользователя {or_press_back}"
notify_everyone = "🔔Оповещение всем пользователям"
input_notification = f"Введите текст оповещения {or_press_back}"


def confirm_notification(text: str) -> str:
    return f"Вы уверены, что хотите отправить оповещение?\nТекст:\n{text}"


def notification_sent(done_users: int, total_users: int) -> str:
    return f"Оповещение успешно отправлено {done_users}/{total_users} пользователям."


manager_panel = "📦 Управление заказами"
manager_orders = "📁 Заказы"
remove_manager_role = "👨‍💼 Убрать роль менеджера"
add_manager_role = "👨‍💼 Сделать менеджером"
remove_admin_role = "🔴 Убрать роль администратора"
add_admin_role = "🔴 Сделать администратором"


def change_order_status(status):
    return f'Изменить статус на "{status}"'


# Shop stats
registration_stats = "👥Статистика регистраций"
order_stats = "📦Статистика заказов"
all_time = "За всё время"
monthly = "За последние 30 дней"
weekly = "За последние 7 дней"
daily = "За последние 24 часа"

# Payment settings
yoomoney = "🟢 ЮMoney"
qiwi = "🏧 QIWI"


# Shop settings
main_settings = "🛠️ Основные настройки"
item_settings = "🗃️ Настройки товаров"
payment_settings = "💳 Настройки оплаты"
additional_settings = "📖 Дополнительные настройки"
custom_commands = "📖 Команды"
add_command = "📝 Добавить команду"
clean_logs = "📖 Очистить логи"
clean_logs_text = "⚠️ Вы уверены, что хотите очистить логи? Они будут удалены без возможности восстановления!\n(Логи за сегодняшний день не будут удалены)"
backups = "💾 Резервное копирование"
update_backup = "🔄 Обновить резервную копию"
load_backup = "💿 Загрузить резервную копию"
clean_backups = "🧹 Очистка резервных копий"
system_settings = "💻 Настройки системы"
clean_images = "🗑️ Удалить неиспользуемые изображения"
clean_images_text = "⚠️ Вы уверены, что хотите удалить неспользуемые изображения? Они будут удалены без возможности восстановления!"
clean_database = "📚 Очистить базу данных"
clean_database_text = "⚠️ Вы уверены, что хотите очистить базу данных? Все данные будут удалены без возможности восстановления!"
reset_settings = "⚙️ Сбросить настройки"
resert_settings_text = "⚠️ Вы уверены, что хотите сбросить настройки? Все данные будут удалены без возможности восстановления!"
image = "🖼️ Изображение"
checkout_settings = "🛒 Настройки оформления заказа"
stats_settings = "📈 Настройки статистики"
graph_color = "🌈 Цвет графика"
border_width = "🔲 Ширина обводки"
title_font_size = "ℹ️ Размер названия графика"
axis_font_size = "↔️Размер текста для осей"
tick_font_size = "🔢Размер текста для делений"
unavailable = "⛔️"
minus = "➖"
plus = "➕"
enable_sticker = "❌ Стикер в приветствии"
disable_sticker = "✅ Стикер в приветствии"

toggle_email = "Email при заказе"
toggle_phone_number = "Номер телефона при заказе"
enable_delivery = "❌ Доставка"
disable_delivery = "✅ Доставка"
toggle_captcha = "CAPTCHA при заказе"
enable_debug = "❌ Режим отладки"

input_email = f"Введите email {or_press_back}"
input_phone = f"Введите номер телефона {or_press_back}"
input_address = f"Введите адрес {or_press_back}"
input_captcha = f"Введите CAPTCHA {or_press_back}"
input_captcha_error = "Неверный CAPTCHA"
input_email_error = "Неверный email"
input_phone_error = "Неверный номер телефона"

input_delivery_price = f"💰 Введите стоимость доставки {or_press_back}"
change_delivery_price = "💰 Изменить стоимость доставки"
disable_debug = "✅ Режим отладки"

# input_comment = "✅ Заказ создан. В ближайшее время с вами свяжется менеджер."
confirm_order = "✅ Заказ создан. В ближайшее время с вами свяжется менеджер."

# Manager tab
view_order = "📂 Посмотреть заказ"
