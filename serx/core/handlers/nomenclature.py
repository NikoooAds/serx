from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from core.database.dbworker import Request
from core.handlers import view
from core.keyboards.nomenclature import inline, reply

nm_router = Router()


@nm_router.message(Command("nomen"))
async def cmd_nomen(msg: Message):
    await msg.answer(f"Nomenclature")


@nm_router.message(F.text.startswith("back"))
async def cmd_back(msg: Message, req: Request, bot: Bot):
    await msg.answer("/help")


@nm_router.message(F.text == "НОМЕНКЛАТУРА")
async def cmd_nomenclature(msg: Message, req: Request):
    records = await req.get_nomenclature()

    nm_kb = inline.get_nomenclature_kb()

    for r in records:
        nm_kb.inline_keyboard.append(
            [inline.get_nomenclature_button(r["code"], r["description"])],
        )
    nm_kb.inline_keyboard.extend([inline.get_nm_footer()])

    await msg.answer(
        f"{msg.from_user.full_name} выберите нужную номенклатуру.",
        reply_markup=nm_kb,
    )


@nm_router.callback_query(F.data.startswith("nomenclature_"))
async def cmd_nm_action(callback: CallbackQuery, req: Request, bot: Bot):
    msg = callback.data.split("_")[1]


@nm_router.message(F.text)
async def cmd_not_valid(msg: Message):
    await msg.reply(f"Нет такой команды")
