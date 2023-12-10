from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def available_commands(bot: Bot):
    commands = [
        # BotCommand(command="start", description="Staring commands"),
        BotCommand(command="view", description="Меню выбора проверки"),
        BotCommand(command="help", description="Помощь в использовании"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
