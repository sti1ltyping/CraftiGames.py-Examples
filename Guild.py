from CraftiGames import Pikanetwork, PikaAnnotations
import asyncio


Guild: str = ... # Name of the guild

async def example():

    async with Pikanetwork() as api:

        guild = await api.Guild(Guild)
    
    if guild is None:
        return print("Guild not found!")
    
    name = guild.name
    tag = guild.tag
    level = guild.level
    member_list = guild.member_list
    member_count = guild.member_count
    leader = guild.leader

    # and more...

    print(name, tag, level, member_count, leader)
    print(member_list)

asyncio.run(example())
