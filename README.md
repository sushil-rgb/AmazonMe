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
Welcome to AmazonMe, a web scraper designed to extract information from the Amazon website and store it in a MongoDB databse. This repository contains
the code for the scraper, which utilizes the Requests and BeautifulSoup libraries to automate the scraping process. The scraper also leverages
asyncio concurrency to efficiently extract thousands of data points from the website.

## Install necessary requirments:
It's always a good practice to install a virtual environment before installing necessary requirements:
```python
python.exe -m venv environmentname
environmentname/scripts/activate
```
Install necessary requirements:
```python
  pip install -r requirements.txt
```

## Usage
```python
  async def main():
    base_url = ""  # Enter a desired URL product category of your choice:
    mongo_to_db = await export_to_mong(base_url)
    return mongo_to_db
```

# To run the script, go to terminal and type:
```python
  python main.py
```
<p align = 'center'><i>Demo of the scraper scraping the content from Amazon</i></p>
<p align = 'center'><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmNmZjFmNzlkMmZhMGI3ZTVmZTc1MDFiNmZhMDAyOTFmOTI2YTU0ZCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/z1yvTb9gwvuZG9N0Xz/giphy.gif" alt="Discord bot"></p>

## Features
Upon executing the program, the scraper commences its operation by extracting the following fields and storing the required product information in Mongo databases.<br>
<ul>
  <li><b>Product</b></li>
  <li><b>ASIN</b></li>
  <li><b>Price</b></li>
  <li><b>Original price</b></li>
  <li><b>Review</b></li>
  <li><b>Review count</b></li>
  <li><b>Hyperlink</b></li>
  <li><b>Image url</b></li>
</ul>

### MongoDB Integration
Newly added to AmazonMe is the integration with MongoDB, allowing you to store the scraped data in a database for further analysis or usage. The scraper can now save the scraped data directly to a MongoDB database.

To enable MongoDB integration, you need to follow these steps:

1. Make sure you have MongoDB installed and running on your machine or a remote server.
2. Install the `pymongo` package by running the following command:
                   <p align = 'center'>
                    ```python
                       pip install pymongo
                    ```
                    </p>
3. In the script or module where you handle the scraping and data extraction, import the `pymongo`
With the MongoDB integration, you can easily query and retrieve the scraped data from the database, perform analytics, or use it for other purposes.

## Note
Please note that the script is designed to work with Amazon and may not work with other types of websites. Additionally, the script may be blocked by the website if it detects excessive scraping activity, so please use this tool responsibly and in compliance with Amazon's terms of service

If you have any issues or suggestions for improvements, please feel free to open an issue on the repository or submit a pull request.

## License
This project is licensed under GPL-3.0 license. This scraper is provided as-is and for educational purposes only. The author is not repsonsible for any damages or legal issues that may result from its user. Use it at your own risk. Thank you for using the AmazonMe!

