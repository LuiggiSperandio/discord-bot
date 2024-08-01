import discord
from os import environ
from time import sleep
import re
from random import randint
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'Message from {message.author}: {message.content}')
    # await message.channel.send(f'<@{message.author.id}> e tu que é gay mlk')


    #ban hammer
    if re.search('^!roleta.*', message.content.lower()):
        if len(message.mentions) == 0:
            await message.add_reaction('🫏')
            # await message.channel.send(f'🫏<@{message.author.id}> Tem que marcar alguém né sua mula🫏')
            await message.channel.send(f'<@{message.author.id}> Atirou nele mesmo 🫏')
            await message.author.edit(voice_channel=None)
        if len(message.mentions) > 0:
            if client.user in message.mentions:
                await message.add_reaction('💩')
                await message.channel.send(f'<@{message.author.id}> 💩🔫🤖 Tentou atirar no bot e se fodeu!')
                await member.edit(voice_channel=None)
            else:
                a=0
                for member in message.mentions:
                    if a == 0 and randint(1,20) == 10:
                        a=1
                        await message.add_reaction('💣')
                        await message.channel.send(f'Bot errou e acertou o <@{message.author.id}>!')
                        await message.author.edit(voice_channel=None)
                    elif a == 0 and randint(1,10) == 5:
                        a=1
                        await message.add_reaction('🔫')
                        await message.channel.send(f'<@{member.id}>🔫🤖')
                        await member.edit(voice_channel=None)
                if a == 0:
                    await message.add_reaction('🤣')
                    await message.channel.send(f'Hoje não <@{message.author.id}>!')



client.run(environ['TOKEN'])