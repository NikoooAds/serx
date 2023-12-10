import asyncio
import logging

import asyncpg
from aiogram import Bot, Dispatcher
from core.handlers import view
from core.middlewares.dbsession import DbSession
from core.settings import settings
from core.utils import info


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] %(name)s - %(message)s",
    )

    bot = Bot(token=settings.bot.bot_token, parse_mode="HTML")

    pool_connect = await asyncpg.create_pool(
        host=settings.db.host,
        port=settings.db.port,
        database=settings.db.database,
        user=settings.db.user,
        password=settings.db.password,
        command_timeout=60,
    )

    dp = Dispatcher()

    # Registor update middleware for db
    dp.update.middleware.register(DbSession(pool_connect))

    dp.startup.register(info.startup_app)

    # Routers
    dp.include_router(view.router)

    dp.shutdown.register(info.shutdown_app)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
