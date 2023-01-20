<p align='center'>
  <a href='https://www.amazon.com'><img src='https://miro.medium.com/max/799/1*Sjalm0U8yZgRBMmRVuGGLQ.png'></a>
</p>


# AmazonMe
Welcome to the AmazonMe scraper that scrape Amazon product database and save it into excel database. This repository contains the code for a web scraper that can extract information from the Amazon website. The scraper uses the Python Playwright library to automate the process of browsing and extracting data from the website.
To get started, you will need to have Python and the necessary requirements installed on your machine.

## Install virtual environment:
It's always a good practice to install a virtual environment before installing necessary requirements:
```python
python.exe -m venv environmentname
environmentname/scripts/activate
```

## Install necessary requirements:
```python
pip install -r requirements.txt
playwright install
```

## The repository includes the following files:
**scraper.py**: This is the main script that initiate the automation.<br>
**tools.py**: This file contains the main code for the scraper.

## To run the script, go to terminal....
```python
python scraper.py
```

## Features
After running the program, the scraper will ask you to enter a product url. Do it accordingly and it will scrape the data such as<br>
**Product name**, **ASIN**, **Prices**, **Reviews**, **Links**

## Note
Please note that the script is designed to work with Amazon and may not work with other types of websites. Additionally, the script may be blocked by the website if it detects excessive scraping activity, so please use this tool responsibly and in compliance with Amazon's terms of service

If you have any issues or suggestions for improvements, please feel free to open an issue on the repository or submit a pull request.

## License
This project is licensed under GPL-3.0 license. This scraper is provided as-is and for educational purposes only. The author is not repsonsible for any damages or legal issues that may result from its user. Use it at your own risk. Thank you for using the AmazonMe!


