import discord
import time
from discord.member import VoiceState
import xlrd
from xlwt import Workbook
from discord.ext import commands
import csv



CHANNEL_ID=int(763390600103854114)
VOICE_ID=int(843865682760302602)
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	print('Bot is Ready.')
	channel = client.get_channel(CHANNEL_ID)
	await channel.send("MUN Bot isLive")


#FUNCTIONS
@client.command()            
async def ping(ctx):
	await ctx.send(f'What do you expect, Pong?\nLatency= {round(client.latency*1000)}ms')
	print(ctx.author)
	print(ctx.author.id)


@client.command()    
async def Attendence(ctx, nys):

	#New Code From Here
	print(nys.split(','))
	info=nys.split(',')
	
	with open('attendees.csv','a',newline='') as file:
		fieldnames=["Name","Stream","Year"]
		writer=csv.DictWriter(file,fieldnames=fieldnames)
		writer.writerow({"Name":info[0],"Stream":info[1],"Year":info[2]}) 
	await ctx.send(f'{nys}, noted')


@client.command(pass_context=True)    
async def join(ctx):
	vcchannel=client.get_channel(VOICE_ID)
	await vcchannel.connect()
	await ctx.send("Joined!")

@client.command(pass_context=True)    
async def leave(ctx):
	await ctx.guild.voice_client.disconnect()
	await ctx.send("Left!")

@client.command(pass_context=True)
async def att(ctx):
	vcchannel=client.get_channel(VOICE_ID)
	try:
		user = ctx.message.author
		vc = user.voice.channel
		if (vc == vcchannel):
			await ctx.send(f'**{ctx.author}**, Attendance Recorded')
	except:
		await ctx.send(f'**{ctx.author}**, You must be in the Meeting')

client.run(TOKEN)
