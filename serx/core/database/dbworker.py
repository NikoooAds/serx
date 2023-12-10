import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_user(self, user_id: int, username: str, full_name: str):
        query = (
            f"INSERT INTO users (user_id, username, full_name) "
            f"VALUES ({user_id}, '{username}', '{full_name}') ON CONFLICT (user_id) "
            f"DO UPDATE SET username='{username}',full_name='{full_name}'"
        )

        await self.connector.execute(query, timeout=60)
