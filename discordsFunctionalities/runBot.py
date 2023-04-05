import re
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
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} {channel}.')

        asin_pattern = r"""^[A-Z0-9]{10}$"""
        regex_pattern = """^hi|hello|hey|yo"""
        amazon_pattern = '(https?://)?(www\.)?amazon\.(com|in|co\.uk)/.+'
        if message.guild is None and re.match(regex_pattern, message.content, re.IGNORECASE):
            await message.author.send(f"Hey {username}. Type '!help' to know the list of commands.")
        elif message.content == '!help':
            await message.author.send('Paste the Amazon products link to know the ASIN or ISBN respectively.\nPaste the ASIN/ISBN to get the product details.')
        elif message.guild is None and re.search(amazon_pattern, user_message):        
            await asin_isbn(message.author, user_message)
        elif message.guild is None and (re.match(asin_pattern, message.content)):
            await export_to_db(user_message)
            await message.author.send('Please wait. Fetching data from Amazon.')            
            await getdataByasin(user_message, message.author)           
        else: 
            await message.author.send(f"Invalid link. Please try a valid Amazon product link.")              

    client.run(Token)

