from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_nomenclature_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            # [InlineKeyboardButton(text="Macbook 15", callback_data="apple_air_15")],
        ]
    )
    return kb


def get_nomenclature_button(code: int, description: str):
    button = InlineKeyboardButton(text=f"{code} {description}", callback_data=f"{code}")

    return button


def get_nm_footer():
    footer_buttons = [
        InlineKeyboardButton(text="<", callback_data="nomenclature_prev"),
        InlineKeyboardButton(text="Back", callback_data="nomenclature_back"),
        InlineKeyboardButton(text=">", callback_data="nomenclature_next"),
    ]

    return footer_buttons
