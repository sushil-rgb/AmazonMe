import datetime
import discord
import sys
import os

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon


async def on_ready():
    """
    This function prints a message when the bot is ready to use.
    """
    print(f"Buddy is now running.")


async def asin_isbn(user, userInput):
    """
    This function takes a user object and a user input as parameters, calls the Amazon class to get ASIN and ISBN numbers, 
    and sends the results to the user.

    Args:
        -user (discord.User): User object.
        -userInput (str): User input.

    Returns:
        -None
    """
    datas = await Amazon().getASIN(userInput)
    await user.send(datas)


async def getdataByasin(userInput, user):
    """
    This function takes a user input and a suer object as parameters, call the Amazon class to get product data using ASIN, 
    creates a discord embed with the product data, and send the embed to the user.

    Args:
        -userInput (str): User input.
        -user (discord.User): User object.

    Returns:
        -None
    """
    try:
        datas = await Amazon().dataByAsin(userInput)

        name = datas['Name']
        hyperlink = datas['Hyperlink']

        embed = discord.Embed(title=name, url=hyperlink, color=0xff9900)
        embed.add_field(name = 'Price', value = datas['Price'], inline = False)
        embed.add_field(name = 'Availability', value = datas['Availability'], inline = False)
        embed.add_field(name = "Store", value = f"[{datas['Store']}]({datas['Store link']})", inline = False)
        embed.add_field(name = 'Rating', value = datas['Rating'], inline = False)
        embed.add_field(name = 'Review count', value = datas['Rating count'], inline = False)

        embed.set_thumbnail(url = datas['Image'])
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        await user.send(embed = embed)
    except Exception as e:
        await user.send('Content loading error. Please try again in few minutes.')

