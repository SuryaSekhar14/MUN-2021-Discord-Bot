import discord
import time
import random
import xlsx
from discord.ext import commands

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
	print('Bot is Ready.')

#FUNCTIONS

