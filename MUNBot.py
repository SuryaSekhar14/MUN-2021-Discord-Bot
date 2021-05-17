import discord
import time
import random
#import xlsx
from discord.ext import commands

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
	print('Bot is Ready.')

#FUNCTIONS

#Check Ping
@client.command()    
async def noice(ctx):
	await ctx.send(f'Noice.\n{round(client.latency*1000)}ms')






client.run('ODQzNzg2MDYyMTQ0ODY0MjY2.YKI7Ag.fxIZrjAexauw_TEaN7Y-lkG-JR4')
