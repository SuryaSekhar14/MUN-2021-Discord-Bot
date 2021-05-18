import discord
import time
from discord.member import VoiceState
from discord.ext import commands
import csv


TOKEN = ''
CHANNEL_ID=int(829356662665642067)
VOICE_ID=int(829356662665642068)
client = commands.Bot(command_prefix = '')

@client.event
async def on_ready():
	print('Bot is Ready.')
	channel = client.get_channel(CHANNEL_ID)
	await channel.send("MUN Bot is Live")


#FUNCTIONS
@client.command()            
async def ping(ctx):
	await ctx.send(f'What do you expect, Pong?\nLatency= {round(client.latency*1000)}ms')
	print(ctx.author)

@client.command()    
async def Attendance(ctx, *nys):
	inter=list(nys)
	info=inter
	n=len(info)
	vcchannel=client.get_channel(VOICE_ID)
	try:
		#############
		user = ctx.message.author
		vc = user.voice.channel
		if (vc == vcchannel):
			with open('attendees.csv','a',newline='') as file:
				fieldnames=["Name","Stream","Year","Team"]
				writer=csv.DictWriter(file,fieldnames=fieldnames)
				if(n==4):
					writer.writerow({"Name":info[0],"Stream":info[1],"Year":info[2],"Team":info[3]})
				if(n==5):
					writer.writerow({"Name":info[0]+' '+info[1],"Stream":info[2],"Year":info[3],"Team":info[4]}) 
				if(n==6):
					writer.writerow({"Name":info[0]+' '+info[1]+' '+info[2],"Stream":info[3],"Year":info[4],"Team":info[5]})
				if(n==7):
					writer.writerow({"Name":info[0]+' '+info[1]+' '+info[2]+' '+info[3],"Stream":info[4],"Year":info[5],"Team":info[6]})
			#############
			await ctx.send(f'**{info[0]}**, Attendance Recorded')
		else:
			await ctx.send(f'**{info[0]}**, you are in another Voice Channel')
	except:
		await ctx.send(f'**{info[0]}**, You must be in a Voice Channel')

@client.command(pass_context=True)    
async def join(ctx):
	vcchannel=client.get_channel(VOICE_ID)
	await vcchannel.connect()
	await ctx.send("Joined!")

@client.command(pass_context=True)    
async def leave(ctx):
	try:
		await ctx.guild.voice_client.disconnect()
		await ctx.send("Left the Meeting")
	except:
		await ctx.send("I am not in the Meeting.")

# att() commented out, if required later shall be used.
'''@client.command(pass_context=True)
async def att(ctx):
	vcchannel=client.get_channel(VOICE_ID)
	try:
		user = ctx.message.author
		vc = user.voice.channel
		if (vc == vcchannel):
			await ctx.send(f'**{ctx.author}**, Attendance Recorded')
		else:
			await ctx.send(f'**{ctx.author}**, you are in another Voice Channel')
	except:
		await ctx.send(f'**{ctx.author}**, You must be in a Voice Channel')
'''

client.run(TOKEN)
