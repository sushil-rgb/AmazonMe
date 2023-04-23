import os
import sys
import discord
import datetime

sys.path.append(os.getcwd())
from scrapers.scraper import Amazon


async def on_ready():
    print(f"Buddy is now running.")


async def asin_isbn(user, userInput):
    datas = await Amazon().getASIN(userInput)
    await user.send(datas)


async def getdataByasin(userInput, user):
    datas = await Amazon().dataByAsin(userInput)
    try:
        embed = discord.Embed(title=datas['Name'], url=datas['Hyperlink'], color=0xff9900)
        embed.add_field(name = 'Price', value = datas['Price'], inline = False)
        embed.add_field(name = 'Availability', value = datas['Availability'], inline = False)
        embed.add_field(name = "Store", value = f"[{datas['Store']}]({datas['Store link']})", inline = False)
        embed.add_field(name = 'Rating', value = datas['Rating'], inline = False)
        embed.add_field(name ='Review count', value = datas['Rating count'], inline = False)
        embed.set_thumbnail(url = datas['Image'])
        embed.timestamp = datetime.datetime.now()
        embed.set_footer(text = 'Powered by Python', icon_url = 'https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png')
        await user.send(embed = embed)
    except TypeError:
        await user.send("Content loading error. Please try again in few minutes.")    

    
