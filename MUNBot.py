import discord
import time
from discord.member import VoiceState
import xlrd
import env
from xlwt import Workbook
from discord.ext import commands
import csv


TOKEN='ODQzNzg2MDYyMTQ0ODY0MjY2.YKI7Ag.EA0pBFPgYyVlxBM0hwAuF1NTX4Q'
CHANNEL_ID=int(763390600103854114) #channel_id change required
VOICE_ID=int(843865682760302602) #voice_id change required
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	print('Bot is Ready.')

#FUNCTIONS
@client.command()            
async def noice(ctx):
	await ctx.send(f'Noice.\n{round(client.latency*1000)}ms')
	print(ctx.author)
	print(ctx.author.id)
	print(ctx.voice_client)


@client.command()    
async def Attendence(ctx, name, year, stream):

	#New Code From Here
	print(name,year,stream)
	with open('attendees.csv','a',newline='') as file:
		fieldnames=["Name","Stream","Year"]
		writer=csv.DictWriter(file,fieldnames=fieldnames)
		writer.writerow({"Name":name,"Stream":stream,"Year":year})
	await ctx.send(f'{name}, noted')


@client.command(pass_context=True)    
async def join(ctx):
	vcchannel=client.get_channel(VOICE_ID)
	await vcchannel.connect()
	user = ctx.message.author
	vc = user.voice.channel
	print(vc)
	if (vc == vcchannel):
		await ctx.send(f'**{ctx.author}**, Attendance Recorded')
	await ctx.send("Joined!")

@client.command(pass_context=True)    
async def leave(ctx):
	await ctx.guild.voice_client.disconnect()
	await ctx.send("Left!")


client.run(TOKEN)
