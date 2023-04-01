import re
import os
import sys
import discord

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)


async def on_ready():
    print(f"Buddy is now running.")


async def asin_isbn(userInput):
    datas = await Amazon().getASIN(userInput)    
    return datas


async def send_message(message):
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username} said: {user_message} {channel}.')

    regex_pattern = """^hi|hello|hey|yo"""
    if message.guild is None and re.match(regex_pattern, message.content):
        await message.author.send(f"Hey {username}. Type '!help' to know the list of commands.")
    elif message.content == '!help':
        await message.author.send('Paste the Amazon products link to know the ASIN or ISBN respectively.')
    elif message.guild is None and message.content.startswith('https://www.amazon.com/'):
        await message.author.send('Please wait.')
        datas = await asin_isbn(user_message)
        await message.author.send(datas)
    elif message.guild is None: 
        await message.author.send(f"Invalid link. Please try a valid Amazon product link.")
    else:
        pass
    
    

    