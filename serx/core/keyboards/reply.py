from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_kb():
    buttons = [
        [
            KeyboardButton(text="ДАТА"),
            KeyboardButton(text="МАГАЗИН"),
        ],
        [
            KeyboardButton(text="НОМЕНКЛАТУРА"),
        ],
        [
            KeyboardButton(text="ПРОВЕРИТЬ"),
        ],
    ]

    start_reply_kb = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Введите команду или выберите кнопку ↓",
        selective=True,
    )

    return start_reply_kb
