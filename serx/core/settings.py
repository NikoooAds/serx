from dataclasses import dataclass

from environs import Env


@dataclass
class Bots:
    bot_token: str
    admin_id: int


@dataclass
class DBConfig:
    host: str
    port: int
    database: str
    user: str
    password: str


@dataclass
class Settings:
    bot: Bots
    db: DBConfig


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bot=Bots(bot_token=env.str("BOT_TOKEN"), admin_id=env.int("ADMIN_ID")),
        db=DBConfig(
            host=env.str("POSTGRES_HOST"),
            port=env.int("POSTGRES_PORT"),
            database=env.str("POSTGRES_DATABASE"),
            user=env.str("POSTGRES_USER"),
            password=env.str("POSTGRES_PASSWORD"),
        ),
    )


settings = get_settings("/home/fusion/project/serx/serx/core/misc/.envs")

if __name__ == "__main__":
    print(settings)
