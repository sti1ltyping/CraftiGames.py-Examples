from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio


Players: list = [...] # List of players

async def example():

    async with Pikanetwork() as api:
        response = await api.MultiStats(Players, "bedwars", "total", "all_modes")
    
    for username, stats in response:

        # Error handling
        if stats is None:
            print(f"Couldn't find {username}")      # Maybe hidden from the api or incorrect username
            continue

        print(username, stats.wins)
        

asyncio.run(example())
