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
    print(f'{message.author}@{message.channel}: {message.content}', flush=True)
    print('-------------------------', flush=True)

    # get_user_id:
    if re.search('^!user.*', message.content.lower()):
        for user in message.mentions:
            await message.channel.send(f'{user.name}:  {user.id}')


    # ban hammer a.k.a. !roleta
    if re.search('^!roleta.*', message.content.lower()):
        if len(message.mentions) == 0:
            await message.add_reaction('🫏')
            await message.channel.send(f'🫏<@{message.author.id}> Tem que marcar alguem mula! Vai ser kickado só pra ficar ligado. 🫏')
            await message.author.edit(voice_channel=None)
            return
        if len(message.mentions) > 0:
            if discord.utils.get(client.get_all_members(), id=message.author.id) == None:
                await message.add_reaction('💩')
                await message.channel.send(f'<@{message.author.id}> Vai ficar kickando os outros desconectado?')
                for i in range(10):
                    await message.channel.send(f'<@{message.author.id}> arrombex')
                return
            if client.user in message.mentions:
                await message.add_reaction('💩')
                await message.channel.send(f'<@{message.author.id}> 💩🔫🤖 Tentou atirar no bot e se fodeu!')
                await message.author.edit(voice_channel=None)
                return
            else:
                participants = [x for x in message.mentions]
                for i in message.mentions:
                    participants.append(message.author)
                the_chosen_one = choice(participants)
                if the_chosen_one == message.author:
                    await message.add_reaction('💣')
                    await message.channel.send(f'💣<@{the_chosen_one.id}>💣')
                    await the_chosen_one.edit(voice_channel=None)
                    return
                await message.add_reaction('🔫')
                await message.channel.send(f'<@{the_chosen_one.id}>🔫🤖')
                await the_chosen_one.edit(voice_channel=None)
                return
    
    # Music Check
    if re.search('!play.*', message.content.lower()):
        await message.channel.send(f'<@{message.author.id}> https://spotify.com/download')
        return
    
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
                return
            await message.channel.send(f'Vai ficar mandando postizinho do {medium[:-4]} no chat? <@{message.author.id}>')
            return


# Kick when join channel
@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None and (after.channel != before.channel):
        if randint(1,3) == 2:
            # memes id:                  875435905148661760
            channel = client.get_channel(875435905148661760)
            await channel.send(f'<@{member.id}> Oléééééé')
            await member.edit(voice_channel=None)
            print(f'{member} kicked OMEGALUL', flush=True)
            return


client.run(environ['TOKEN'])