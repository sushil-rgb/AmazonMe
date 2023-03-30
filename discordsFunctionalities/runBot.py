import os
import sys
import discord
from dotenv import load_dotenv

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon


load_dotenv(f"{os.getcwd()}//environmentVariables//.env")
Token = os.getenv('MY_TOKEN')
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)


def run_discord_bot():
    @client.event
    async def on_ready():
        print(f"Buddy is now running.")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: {user_message} {channel}.")

        if message.guild is None and message.content.startswith('https://www.amazon.com/'):
            asin = await Amazon().getASIN(user_message)
            await message.author.send(asin)
        else:
            await message.author.send(f"Invalid link. Please try a proper valid Amazon product link.")
        
        if message.guild is None and message.content.startswith('hi'):
            await message.author.send(f"hey {username}")
    
    client.run(Token)