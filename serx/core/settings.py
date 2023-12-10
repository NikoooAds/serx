from dataclasses import dataclass

from environs import Env


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bot: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bot=Bots(bot_token=env.str("BOT_TOKEN"), admin_id=env.int("ADMIN_ID")),
    )


settings = get_settings("/home/fusion/project/serx/serx/core/misc/.envs")

if __name__ == "__main__":
    print(settings)
