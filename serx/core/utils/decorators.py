from aiogram import Bot
from aiogram.types import Message
from core.database.dbworker import Request


def auth_is_member(func):
    async def wrapper(msg: Message, req: Request, bot: Bot, *args, **kwargs):
        user = await req.check_roles(msg.from_user.id)
        if not user[0]["isActive"]:
            return await msg.reply("Access Denied. You're not a member", reply=False)
        return await func(msg, req, bot, *args, **kwargs)

    return wrapper


def auth_is_admin(func):
    async def wrapper(msg: msg, req: Request, bot: Bot):
        user = await req.check_roles(msg.from_user.id)
        if not user[0]["isAdmin"]:
            return await msg.reply("Access Denied. You're not an admin", reply=False)
        return await func(msg, req, bot)

    return wrapper


def is_blocked(func):
    async def wrapper(msg: msg, req: Request):
        user = await req.check_roles(msg.from_user.id)
        if not user[0]["isBlocked"]:
            return await msg.reply("Access Denied. You're blocked", reply=False)
        return await func(msg, req, bot)

    return wrapper
