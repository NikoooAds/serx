from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["start", "run"]))
async def cmd_start(message: Message):
    await message.answer("Start message")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(f"Future helper message")
