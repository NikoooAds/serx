from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from core.database.dbworker import Request
from core.handlers.router2 import nm_router
from core.handlers.router3 import nm_router_3
from core.keyboards.reply import get_main_kb
from core.utils.menu import available_commands

main_router = Router()

users = dict()
# main_router.include_router(nm_router_3)
main_router.include_router(nm_router)


@main_router.message(CommandStart())
async def cmd_start(msg: Message, req: Request, bot: Bot):
    await req.add_user(  # Update fields if exist
        msg.from_user.id, msg.from_user.username, msg.from_user.full_name
    )

    if msg.from_user.id not in users:
        users[msg.from_user.id] = {
            "full_name": msg.from_user.full_name,
        }
        await cmd_help(msg)

    else:
        await msg.answer(f"You have dict :{ users[msg.from_user.id]}")


@main_router.message(Command("view"))
async def cmd_main_view(msg: Message, req: Request, bot: Bot):
    await available_commands(bot)  # Menu for quick move

    date = users[msg.from_user.id].get("date", 0)
    if date == 0:
        date = datetime.now().strftime("%d.%m.%Y")

    await msg.answer(
        f"Добрый день, <b>{msg.from_user.full_name}</b>! (Ваш ID: {msg.from_user.id})\n"
        f"Если Вам необходима помощь, нажмите /help в меню.\n"
        f"Дана: {date} г.\n"
        f"Магазин: <i>не указано</i>\n"
        f"Номенклатура: <i>не указана</i>\n",
        reply_markup=get_main_kb(),
    )


@main_router.message(Command("help"))
async def cmd_help(msg: Message):
    await msg.answer(
        f"Данный бот содан для компании Serx"
        f"Для проверки продукции Вам необходимо:\n- Выбрать номенклатуру\n- Выбрать магазин\n"
        f"\nДля выбора продукции выберите пункт /view в меню\n"
        f"Для <b>выбора</b> необходимой номенклатуры, даты или\n"
        f"магазина нажмите кнопку с соответствующим названием\n"
        f"После выбора параметров проверки нажмите кнопку проверить\n"
        f"и следуйте дальнейшей инструкции."
    )
