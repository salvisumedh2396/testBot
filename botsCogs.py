import discord
import random
#when the bot goes live, load all of the existing cogs from the module
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

#we have created a client here
client = commands.Bot(command_prefix='.', intents=intents)

#ctx - represents the context
#extension - represents the cog you want to load
#f'cogs.{extension}' - goes into the cogs folder and then searches for the extension
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# os.listdir('') -- it will list out all the directories within a given directory
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODg4MjUyNjA5MDU0NTA3MDE4.YUP_tA.ZkRi9PcX5zFLKk4c8XCFJTZZ76w')