#############################################################
#                                                           #
#          Server status checker thingy                     #
#                                                           #
#          Written by BoredManPlays                         #
#                                                           #
#                                                           #
#############################################################

import discord
from discord import *
import discord.client
import discord.message

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Connected to Discord")
    channel1 = client.get_channel(886229785150369872)  # ID of channel
    embed = discord.Embed(
        title="Initialisation message",
        description="The bot won't work until\nthe server is restarted",
        color=0xF03224,
    )
    sent = await channel1.send(embed=embed)

class Bot(discord.Client):
    def __init__(self):
        discord.Client.__init__(
            self, intents=discord.Intents(guilds=True, members=True)
        )


@client.event
async def on_member_update(before, after):
    if after.id == 804610079423987712 and not (before.status == after.status): # ID of user to monitor
        channel1 = client.get_channel(886229785150369872)  # ID of channel
        msg = await channel1.history().get(author__id=886405787772145714)  # ID of bot
        await msg.delete(delay=1)
        #print(f"Deleted message: {msg.id}")
        if str(after.status) == "offline":
            embed = discord.Embed(
                title="",
                description="**Serverio versija:**\n1.17.1\n\n**Serverio IP:**\n89.40.6.180:20000\n\n**Serverio būsena**:\nIšjungtas",
                color=0xF03224,
            )
            sent = await channel1.send(embed=embed)



        if str(after.status) == "online":
            embed = discord.Embed(
                title="",
                description="**Serverio versija:**\n1.17.1\n\n**Serverio IP:**\n89.40.6.180:20000\n\n**Serverio būsena**:\nĮjungtas",
                color=0x00FF00,
            )
            sent = await channel1.send(embed=embed)



client.run("token")
