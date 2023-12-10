from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_date_kb():
    buttons = [[InlineKeyboardButton(text="Back", callback_data="view_router")]]
    date_kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return date_kb
