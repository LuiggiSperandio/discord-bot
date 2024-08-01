import discord
from os import environ
from time import sleep
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
    print(f'Message from {message.author}: {message.content} | {message.mentions}')
    await message.channel.send(f'@{message.author} e tu que é gay mlk')

    #ban hammer
    if len(message.mentions) > 0:
        for member in message.mentions:
            await member.ban()
            sleep(5)
            await member.unban()


    #Message add_reaction (https://discordpy.readthedocs.io/en/stable/api.html#discord.Message.add_reaction)
    #when ban react with bomb


client.run(environ['TOKEN'])