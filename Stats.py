from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio


Player: str = ... # Username of the player

async def example():

    async with Pikanetwork() as api:

        stats = await api.Stats(Player, "bedwars", "total", "all_modes")
    
    if stats is None:
        return print("Player not found or Player is hidden from the API!")
    
    wins = stats.wins
    losses = stats.losses
    wlr = stats.wlr
    win_rate = stats.win_rate
    beds_destroyed = stats.beds_destroyed

    # and more...

    print(wins, losses, wlr, win_rate, beds_destroyed)

asyncio.run(example())
