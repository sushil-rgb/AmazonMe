import os
import sys
import discord
from .sendMessages import *
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
    async def initiation():
        await on_ready()
    
    @client.event
    async def on_message(message):
        await send_message(message)        
    
    client.run(Token)

