from aiogram import Bot
from core.settings import settings


async def startup_app(bot: Bot):
    """Info message into bot at startup"""
    await bot.send_message(settings.bot.admin_id, text="Bot started!")


async def shutdown_app(bot: Bot):
    """Info message into bot at shutdown"""
    await bot.send_message(settings.bot.admin_id, text="Bot stopped!")
