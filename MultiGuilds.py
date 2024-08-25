from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio

Guilds: list = [...] # List of guilds

async def example():
    async with Pikanetwork() as api:
        response = await api.MultiGuilds(Guilds)

    for name, guild_api in response:
        # Error handling
        if guild_api is None:
            print(f"Couldn't find {name}")  # Incorrect guild name/ guild doesn't exists
            continue

        print(name, guild_api.level)

asyncio.run(example())
