import re

from aiogram import types
from aiogram.filters import Filter


class DateFilter(Filter):
    key = "is_date"

    reg = r"(((0[1-9])|([12][0-9])|(3[01]))[\.\/\*:]{1}((0[0-9])|(1[012]))[\.\/\*:]((20[012]\d|19\d\d)|(1\d|2[0123])))"
    pattern = re.compile(reg)

    async def __call__(self, msg: types.Message) -> bool:
        """Return True if data is correct"""
        return self.pattern.match(msg.text)
