from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio

Player: str = ... # Username of the player
        
async def example():

    # Sending API requests with an asynchronous environment
    async with Pikanetwork() as api:

        profile = await api.Profile(Player)
        
        # You can also get the skin (BYTES) of the player.
        skin = await profile.skin.Default.face()

    if profile is None:
        return print(Player, "has not registered on PikaNetwork.")
    
    username = profile.username
    level = profile.level
    minigame_rank = profile.highest_minigame_rank
    practice_rank = profile.highest_practice_rank
    discord_verified = profile.discord_verified
    

    if discord_verified:
        print(Player, 'has verified their discord account.')

    # Extract the guild from player's profile
    # Returns 'Guild' class if player is in a guild else returns None
    guild = profile.guild() 

    if guild:
        name = guild.name
        leader = guild.leader
        # and more...

        print(f"{username} is a member of {name}. Leader of that guild is {leader}")

    print(username, level, minigame_rank, practice_rank)
        
asyncio.run(example())
