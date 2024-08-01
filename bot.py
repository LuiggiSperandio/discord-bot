import discord
from os import environ
from dotenv import load_dotenv
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if 'bot' in message.content.lower():
            await message.channel.send('Hello World!')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

client.run(environ['TOKEN'])
