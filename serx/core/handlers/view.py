from datetime import datetime

from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from core.database.dbworker import Request
from core.handlers.date import date_router
from core.handlers.market import market_router
from core.handlers.nomenclature import nm_router
from core.keyboards.reply import get_main_kb
from core.utils.decorators import auth_is_member
from core.utils.menu import available_commands

main_router = Router()

users = dict()

main_router.include_router(date_router)
main_router.include_router(market_router)
main_router.include_router(nm_router)


@main_router.message(CommandStart())
async def cmd_start(msg: Message, req: Request, bot: Bot):
    await req.add_user(  # Update fields if exist
        msg.from_user.id, msg.from_user.username, msg.from_user.full_name
    )

    if msg.from_user.id not in users:
        users[msg.from_user.id] = {
            "full_name": msg.from_user.full_name,
            "date": datetime.now().strftime("%d.%m.%Y"),
        }
        await msg.answer("Поля ниже нужно заполнить для дальнейшей проверки!")
        await cmd_main_view(msg, req, bot)

    else:
        await msg.answer(f"Для получения инструкции воспользуйтесь командой /help")


@main_router.message(Command("view"))
@auth_is_member
async def cmd_main_view(msg: Message, req: Request, bot: Bot):
    await available_commands(bot)  # Menu for quick move
    # await msg.answer(f"{msg.text}")
    await msg.answer(
        f"Добрый день, <b>{msg.from_user.full_name}</b>! (Ваш ID: {msg.from_user.id})\n"
        f"Если Вам необходима помощь, нажмите /help в меню.\n"
        f"Дана: {users[msg.from_user.id]['date']} г.\n"
        f"Магазин: <i>не указано</i>\n"
        f"Номенклатура: <i>не указана</i>\n",
        reply_markup=get_main_kb(),
    )


@main_router.message(Command("help"))
@auth_is_member
async def cmd_help(msg: Message):
    await msg.answer(
        f"Это бот содан для компании Serx\n"
        f"Доступные команды:\n"
        f"\n/view - Главное меню выбора номенклатуры и магазина\n"
        f"/help - Помощь в работе с ботом\n"
        f"\nДля проверки продукции Вам необходимо:\n- Выбрать номенклатуру\n- Выбрать магазин\n"
        f"\nДля выбора продукции выберите пункт /view в меню\n"
        f"Для <b>выбора</b> необходимой номенклатуры, даты или\n"
        f"магазина нажмите кнопку с соответствующим названием\n"
        f"После выбора параметров проверки нажмите кнопку <b>ПРОВЕРИТЬ</b> и следуйте дальнейшей инструкции."
    )
