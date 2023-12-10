from aiogram import Bot, F, Router
from aiogram.filters import Command
from aiogram.types import Message
from core.database.dbworker import Request

market_router = Router()


@market_router.message(Command("market"))
async def cmd_get_market(msg: Message):
    await msg.answer(f"Market")
