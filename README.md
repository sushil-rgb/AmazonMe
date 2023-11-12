<p align='center'>
  <a href='https://www.amazon.com'><img src='https://miro.medium.com/max/799/1*Sjalm0U8yZgRBMmRVuGGLQ.png'
                                        width='300'
                                        height=auto
                                        ></a>
</p>

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
        base_url = ""
        # Type True if you want to use proxy:
        proxy = False
        if proxy:
            mongo_to_db = await export_to_mong(base_url, f"http://{rand_proxies()}")
        else:
            mongo_to_db = await export_to_mong(base_url, None)
        # sheet_name = "Dinner Plates"  # Please use the name of the collection in your MongoDB database to specify the name of the spreadsheet you intend to export.
        # sheets = await mongo_to_sheet(sheet_name)  # Uncomment this to export to excel database.
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
  <li><b>Asin</b></li>
  <li><b>Description</b></li>
  <li><b>Breakdown</b></li>
  <li><b>Price</b></li>
  <li><b>Deal Price</b></li>
  <li><b>You Saved</b></li>
  <li><b>Rating</b></li>
  <li><b>Rating count</b></li>
  <li><b>Availability</b></li>
  <li><b>Hyperlink</b></li>
  <li><b>Image url</b></li>
  <li><b>Image lists</b></li>
  <li><b>Store</b></li>
  <li><b>Store link</b></li>

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

