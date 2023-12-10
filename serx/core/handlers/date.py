from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from core.database.dbworker import Request
from core.filters.main import DateFilter
from core.keyboards.date import inline

# from core.handlers.view import cmd_main_view, users


date_router = Router()


@date_router.message(F.text.lower() == "дата")
async def cmd_get_date(msg: Message, bot: Bot):
    await msg.answer(
        f"Введите дату провекри в формате: день.месяц.год\nПример: 20.10.2023",
        reply_markup=inline.get_date_kb(),
    )


@date_router.message(DateFilter())
async def cmd_check_date(msg: Message):
    # user_data["date"] = msg.text
    await msg.answer("That date!")


@date_router.callback_query(F.data == "view_router")
async def cmd_go_view(callback: CallbackQuery, req: Request, bot: Bot):
    # await cmd_main_view(callback.message, req, bot)
    await callback.message.answer(text=f"Some info", reply_markup=inline.get_date_kb())
    await callback.answer()
    await callback.message.delete()
