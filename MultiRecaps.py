from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio


Recaps: list = [...] # List of recap ids

async def example():

    async with Pikanetwork() as api:
        response = await api.MultiRecaps(Recaps)
    
    for id, recap_api in response:

        # Error handling
        if recap_api is None:
            print(f"Couldn't find any recap of id: {id}")      # Incorrect id/key
            continue

        print(id, recap_api.winners)
        

asyncio.run(example())
