from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from core.database.dbworker import Request

router = Router()


@router.message(Command(commands=["start", "run"]))
async def cmd_start(msg: Message, req: Request, bot: Bot):
    m = msg.from_user
    await req.add_user(m.id, m.username, m.full_name)

    await msg.answer(f"Start message")


@router.message(Command("help"))
async def cmd_help(msg: Message):
    await msg.answer(f"Future helper message")


@router.message(F.text)
async def cmd_not_valid(msg: Message):
    await msg.reply(f"Нет такой команды")
