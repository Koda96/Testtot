import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.bot(command_prefix = ".")

@client.event
async def on_ready():
	print("Hola")
	await client.change_presence(game=discord.Game(name="Wikikoda"))

@client.event
async def on_message(message):
	if message.content.startswith('.hello'):
		msg = 'Hello how are you'.format(message)
		await client.send_message(message.channel, msg)

client.run(os.getenv('TOKEN'))
