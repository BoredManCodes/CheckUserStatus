#############################################################
#                                                           #
#          Server status checker thingy                     #
#                                                           #
#          Written by BoredManPlays                         #
#                                                           #
#                                                           #
#############################################################

from discord.ext import commands
import discord
from discord import *
# import discord.client
import discord.message

# ensure we grant the required server members intent
intents = discord.Intents().all()
intents.members = True

client = commands.Bot(command_prefix='$', intents=intents)
GUILD = 827079191832297473
# bot = commands.Bot(command_prefix='$')
client.update_mode = False
test_mode = False

if test_mode:
    channel_ID = 886583108546207744
    user_ID = 872143777068904468
    init_msg = "The bot is running in test mode\nIt will monitor the status of pls_ignore"
else:
    channel_ID = 886229785150369872
    user_ID = 804610079423987712
    init_msg = "The bot won't work until\nthe server is restarted"


@client.event
async def on_ready():
    channel1 = client.get_channel(channel_ID)  # ID of channel
    embed = discord.Embed(
        title="Initialisation message",
        description=init_msg,
        color=0xF03224,
    )
    global message
    message = await channel1.send(embed=embed)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to:\n'
        f'{guild.name}(id: {guild.id})\n')


@client.event
async def on_command_error(ctx, error):
    channel1 = client.get_channel(channel_ID)
    print("Error")
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Only the Bot Admin can do that')


# update command
@client.command(name='update', help='Marks the server as updating')
@commands.has_role('Bot Admin')
async def update(ctx):
    # delete any past messages from this bot
    channel1 = client.get_channel(channel_ID)  # ID of channel
    msg = await channel1.history().get(author__id=886405787772145714)  # ID of bot
    await msg.delete(delay=0)  # this is here because sometimes the bot tries to delete the message before there is one

    if not client.update_mode:
        channel1 = client.get_channel(channel_ID)  # ID of channel
        embed = discord.Embed(
            title="Serverio būsena",
            description="Atnaujinimas",
            color=0xFFA500,
        )
        await message.edit(embed=embed)
        client.update_mode = True
        print("Update turned on")
    else:
        channel1 = client.get_channel(channel_ID)  # ID of channel
        embed = discord.Embed(
            title="Serverio būsena",
            description="Neatnaujinama",
            color=0xFFA500,
        )
        await message.edit(embed=embed)
        client.update_mode = False
        print("Update turned off")


@client.event
async def on_member_update(before, after):
    if not client.update_mode:
        channel1 = client.get_channel(channel_ID)
        #print("A member update event occurred")
        if after.id == user_ID and not (before.status == after.status):  # ID of user to monitor
            await channel1.send("detected status change of pls_ignore")
            # delete any past messages from this bot
            channel1 = client.get_channel(channel_ID)  # ID of channel
            msg = await channel1.history().get(author__id=886405787772145714)  # ID of bot
            await msg.delete(
                delay=0)  # this is here because sometimes the bot tries to delete the message before there is one
            mesg = "Name and discriminator of detected user:"
            await channel1.send(mesg)
            # is user offline?
            if str(after.status) == "offline":
                print("Status changed to offline")
                embed = discord.Embed(
                    title="",
                    description="**Serverio versija:**\n1.17.1\n\n**Serverio IP:**\n89.40.6.180:20000\n\n**Serverio būsena**:\nIšjungtas",
                    color=0xF03224,  # red
                )
                await message.edit(embed=embed)

            # is user online?
            if str(after.status) == "online":
                print("Status changed to online")
                embed = discord.Embed(
                    title="",
                    description="**Serverio versija:**\n1.17.1\n\n**Serverio IP:**\n89.40.6.180:20000\n\n**Serverio būsena**:\nĮjungtas",
                    color=0x00FF00,  # green
                )
                await message.edit(embed=embed)
    else:
        print("Not displaying the server status due to update mode being set to true")


client.run("token")
