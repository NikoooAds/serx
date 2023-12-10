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

    async def check_roles(self, user_id):
        query = f"SELECT * FROM users WHERE user_id = {user_id};"

        return await self.connector.fetch(query)

    async def get_nomenclature(self):
        query = f"SELECT * FROM nomenclature;"

        # record = await self.connector.fetch(query)
        return await self.connector.fetch(query)
