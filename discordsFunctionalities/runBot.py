from dotenv import load_dotenv
from .sendMessages import *
import discord
import os
import re


load_dotenv(f"{os.getcwd()}//environmentVariables//.env")
Token = os.getenv('MY_TOKEN')
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)


def run_discord_bot():
    """
    Function to run the Discord bot. Registers the event handlers.
    """

    # Event handler for when the bot ready:
    @client.event
    async def initiation():
        await on_ready()

    # Event handler for when a message is received
    @client.event
    async def on_message(message):
        # Ignore messages ent by the bot itself:
        if message.author == client.user:
            return

        # Extract the username, user message, and channel from the message.
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: {user_message} {channel}.')

        # Define regular expressions to match the message:
        asin_pattern = r"""^[A-Z0-9]{10}$"""
        regex_pattern = """^hi|hello|hey|yo"""
        amazon_pattern = '(https?://)?(www\.)?amazon\.(com|in|co\.uk)/.+'

        # If the message is a greeting and is sent in a direct message:
        if message.guild is None and re.match(regex_pattern, message.content, re.IGNORECASE):
            await message.author.send(f"Hey {username}. Type '!help' to know the list of commands.")

        # If the message is !help and is sent in a direct message:
        elif message.content == '!help':
            await message.author.send('Paste the Amazon products link to know the ASIN or ISBN respectively.\nPaste the ASIN/ISBN to get the product details.')

        # If the message is an Amazon product link and is sent in a direct message:
        elif message.guild is None and re.search(amazon_pattern, user_message):
            await asin_isbn(message.author, user_message)

        # IF the message is an ASIN/ISBN and is sent in a direct message:
        elif message.guild is None and (re.match(asin_pattern, message.content)):
            # await export_to_db(user_message)
            # await message.author.send('Please wait. Fetching data from Amazon.')
            await message.author.send(f"Please wait. Fetching data from Amazon.")
            await getdataByasin(user_message, message.author)

        # If the message is not a valid link and is send in a direct message:
        else:
            await message.author.send(f"Invalid link. Please try a valid Amazon product link.")

    # Run the client with the TOKEN:
    client.run(Token)

