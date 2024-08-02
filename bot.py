import discord
from os import environ
from time import sleep
import re
from random import choice, randint
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
    print(f'Message from {message.author}@{message.channel}: {message.content}', flush=True)

    # ban hammer a.k.a. !roleta
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
                participants = [x for x in message.mentions]
                for i in message.mentions:
                    participants.append(message.author)
                the_chosen_one = choice(participants)
                if the_chosen_one != message.author:
                    await message.add_reaction('🔫')
                    await message.channel.send(f'<@{the_chosen_one.id}>🔫🤖')
                    await the_chosen_one.edit(voice_channel=None)
                else:
                    await message.add_reaction('💣')
                    await message.channel.send(f'💣<@{the_chosen_one.id}>💣')
                    await the_chosen_one.edit(voice_channel=None)
    
    # Music Check
    if re.search('!play.*', message.content.lower()):
        await message.channel.send(f'<@{message.author.id}> https://spotify.com/download')
    
    # Social Media check
    mlist = [
        'instagram.com',
        'facebook.com',
        'reddit.com',
        'twitter.com',
        'x.com',
        'youtube.com',
        'twitch.tv',
        'titktok.com'
    ]
    for medium in mlist:
        if medium in message.content:
            if medium == 'youtube.com' or medium == 'twitch.tv' or medium == 'tiktok.com':
                await message.channel.send(f'Vai ficar mandando videozinho do {medium[:-4]} no chat? <@{message.author.id}>')
            else:
                await message.channel.send(f'Vai ficar mandando postizinho do {medium[:-4]} no chat? <@{message.author.id}>')


# Kick when join channel
@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None and (after.channel != before.channel):
        oda_id = 943904144413044736
        # leo_id = 664623667816169473
        leo_id = 390370312161722369
        if member.id == oda_id or member.id == leo_id:
            if randint(1,2) == 2:
                return
            # memes id:                  875435905148661760
            channel = client.get_channel(875435905148661760)
            await channel.send(f'<@{member.id}> Oléééééé')
            await member.edit(voice_channel=None)
            print(f'{member} kicked OMEGALUL', flush=True)


client.run(environ['TOKEN'])