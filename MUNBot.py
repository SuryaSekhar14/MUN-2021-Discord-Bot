import discord
import time
import random
import xlrd
from xlwt import Workbook
from discord.ext import commands

TOKEN='ODQzNzg2MDYyMTQ0ODY0MjY2.YKI7Ag.2f-Hym6sqMvjMwJzERFb6CmVHP4'
CHANNEL_ID=int(819079476000325674)
VOICE_ID=int(691490232662622312)
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	print('Bot is Ready.')

'''
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

#workbook = xlrd.open_workbook('data.xlsx')
'''

#FUNCTIONS
@client.command()             #Check Ping
async def noice(ctx):
	await ctx.send(f'Noice.\n{round(client.latency*1000)}ms')

@client.command()    
async def Attendence(ctx, name, year, stream):
	#sheet1.write(name, year, stream)
	#wb.save('data.xlsx')
	await ctx.send(f'{name}, noted')

@client.command()    
async def VCheck(ctx):
	


client.run(TOKEN)
