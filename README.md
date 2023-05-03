<p align='center'>
  <a href='https://www.amazon.com'><img src='https://miro.medium.com/max/799/1*Sjalm0U8yZgRBMmRVuGGLQ.png'
                                        width='300'
                                        height=auto
                                        ></a>
</p>


### Discord Integration
The web scraper now has a Discord bot that can extract the ASIN or ISBN of a product from
a link sent in a direct message. To use the bot follow these steps:

1. Invite the bot to your Discord server using this <a href = "https://discord.com/api/oauth2/authorize?client_id=1091094561314582528&permissions=1634235578438&scope=bot">amazonBuddy.</a>
2. Send an Amazon product link to the bot in a direct message.
3. The bot will search the link for an ASIN or ISBN, and respond with the appropriate identifier.
4. If you want to retrieve the product details for a specific ASIN, you can send the ASIN to
the bot in a direct message, and it will repsond with product information.

<p align = 'center'><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWU0YjJjMTEyODBmYzI0Mjk1Mjg1YTdmMTVkYWNiNGM5YWFkNDVkZSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/Jg3cKSlnweCsRp5RC1/giphy.gif" alt="Discord bot"></p>


*The bot is in development and currently works only for US Amazon products on the ".com" domain.*


# AmazonMe
Welcome to the AmazonMe scraper that scrape Amazon product database and save it into excel database. This repository contains the code for a web scraper that can extract information from the Amazon website. The scraper uses the Requests, Beautifulsoup libararyto automate the process of scraping and uses asyncio conncurrency to extract thousands of data from the website.
To get started, you will need to have Python and the necessary requirements installed on your machine.<br>
**The bot currently scrapes 20,000 records under 10 minutes.**

## Install virtual environment:
It's always a good practice to install a virtual environment before installing necessary requirements:
```python
python.exe -m venv environmentname
environmentname/scripts/activate
```

## Usage
```python
  # Enter a desired URL product category of your choice:
  base_url = ""
  
  # To run the script, go to terminal and type:
python main.py
```

## Features
After running the program, the scraper will ask you to enter a product url. Do it accordingly and it will scrape the data such as<br>
**Product name**, **ASIN**, **Prices**, **Reviews**, **Links**

## Note
Please note that the script is designed to work with Amazon and may not work with other types of websites. Additionally, the script may be blocked by the website if it detects excessive scraping activity, so please use this tool responsibly and in compliance with Amazon's terms of service

If you have any issues or suggestions for improvements, please feel free to open an issue on the repository or submit a pull request.

## License
This project is licensed under GPL-3.0 license. This scraper is provided as-is and for educational purposes only. The author is not repsonsible for any damages or legal issues that may result from its user. Use it at your own risk. Thank you for using the AmazonMe!

