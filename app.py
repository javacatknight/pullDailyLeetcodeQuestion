import discord
import os
import siteToScrape

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

#discord event check if bot online
@client.event
async def on_ready():
	print(f'{client.user} is now online!')



@client.event
async def on_message():
	if message.author == client.user
		return
	else:
		if message.content.startswith(f'$!getDaily'):
			await message.channel.send ('''No lol.'''_



#get bot token from .env and run client
client.run(os.getenv('TOKEN'))
