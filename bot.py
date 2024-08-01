import discord
from os import environ
from time import sleep
import re
from random import choice
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
            await message.channel.send(f'🫏<@{message.author.id}> Tem que marcar alguem mula! Vai ser kickado só pra ficar ligado. 🫏')
            await message.author.edit(voice_channel=None)
        if len(message.mentions) > 0:
            if client.user in message.mentions:
                await message.add_reaction('💩')
                await message.channel.send(f'<@{message.author.id}> 💩🔫🤖 Tentou atirar no bot e se fodeu!')
                await message.author.edit(voice_channel=None)
            else:
                participants_list = message.mentions
                for i in message.mentions:
                    participants_list.append(message.author)
                the_chosen_one = choice(participants_list)
                await message.add_reaction('🔫')
                await message.channel.send(f'<@{the_chosen_one.id}>🔫🤖')
                await the_chosen_one.edit(voice_channel=None)

client.run(environ['TOKEN'])