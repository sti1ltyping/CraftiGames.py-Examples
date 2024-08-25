from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio


Players: list = [...] # List of players

async def example():

    async with Pikanetwork() as api:
        response = await api.MultiProfile(Players)
    
    for username, profile in response:

        # Error handling
        if profile is None:
            print(f"Couldn't find {username}")      # Not registered on pikanetwork.
            continue

        print(username, profile.highest_minigame_rank)
        

asyncio.run(example())
