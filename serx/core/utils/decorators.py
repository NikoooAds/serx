from aiogram.types import Message
from core.database.dbworker import Request


def auth_is_member(func):
    async def wrapper(message: Message, request: Request):
        user = await request.check_roles(message.from_user.id)
        if not user[0]["isActive"]:
            return await message.reply(
                "Access Denied. You're not a member", reply=False
            )
        return await func(message)

    return wrapper


def auth_is_admin(func):
    async def wrapper(message: Message, request: Request):
        user = await request.check_roles(message.from_user.id)
        if not user[0]["isAdmin"]:
            return await message.reply(
                "Access Denied. You're not an admin", reply=False
            )
        return await func(message)

    return wrapper


def is_blocked(func):
    async def wrapper(message: Message, request: Request):
        user = await request.check_roles(message.from_user.id)
        if not user[0]["isBlocked"]:
            return await message.reply("Access Denied. You're blocked", reply=False)
        return await func(message)

    return wrapper
