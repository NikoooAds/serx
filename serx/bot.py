import asyncio

from aiogram import Bot, Dispatcher

from core.handlers import view
from core.settings import settings


async def main():
    bot = Bot(token=settings.bot.bot_token, parse_mode="HTML")

    dp = Dispatcher()

    dp.include_router(view.router)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
