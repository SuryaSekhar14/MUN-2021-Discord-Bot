import discord
import time
from discord.member import VoiceState
import xlrd
from xlwt import Workbook
from discord.ext import commands

TOKEN='ODQzNzg2MDYyMTQ0ODY0MjY2.YKI7Ag.2f-Hym6sqMvjMwJzERFb6CmVHP4'
CHANNEL_ID=int(819079476000325674)
VOICE_ID=int(843865682760302602)
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
@client.command()            
async def noice(ctx):
	await ctx.send(f'Noice.\n{round(client.latency*1000)}ms')
	print(ctx.author)
	print(ctx.author.id)
	print(ctx.voice_client)

'''
@client.command()    
async def Attendence(ctx, name, year, stream):
	#sheet1.write(name, year, stream)
	#wb.save('data.xlsx')
	await ctx.send(f'{name}, noted')
'''

@client.command(pass_context=True)    
async def join(ctx):
	vcchannel=client.get_channel(VOICE_ID)
	await vcchannel.connect()
	await ctx.send("Joined!")

@client.command(pass_context=True)    
async def leave(ctx):
	await ctx.guild.voice_client.disconnect()
	await ctx.send("Left!")


client.run(TOKEN)
