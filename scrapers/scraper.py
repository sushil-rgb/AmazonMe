from functionalities.tools import TryExcept, yaml_load, randomTime, userAgents, verify_amazon, create_path
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
import aiohttp
import re
import os


class Amazon:
    """
    The Amazon class provides methods for scraping data from Amazon.com.
    
    Attributes:
        headers (dict): A dictionary containing the user agent to be used in the request headers.
        catch (TryExcept): An instance of TryExcept class, used for catchig exceptions.
        scrape (yaml_load): An instance of the yaml_load class, used for selecting page elements to be scraped.
    """
    
    def __init__(self):
        """
        Initializes an instance of the Amazon class.
        """
        self.headers = {'User-Agent': userAgents()}
        self.catch = TryExcept()
        self.scrape = yaml_load('selector')
        
    
    async def static_connection(self, url):
        """
        Sends a GET request to the given URL and returns the reponse content.
        
        Args:
            url (str): The URL to send the GET request to.
        
        Returns:
            bytes: The response content in bytes.
            
        Raises:
            aiohttp.ClientError: If an error occurs while making the request.
        """        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers = self.headers) as resp:
                content = await resp.read()
                return content
    
    
    async def num_of_pages(self, url):
        """
        Returns the number of pages of search results for the given URL.
        
        Args:
            url (str): The URL to determine the number of search result pages for.
        
        Returns:
            int: The number of pages of search results.
        """
        content = await self.static_connection(url)
        soup = BeautifulSoup(content, 'lxml')
        
        # Try except clause for index error, this happens if there are only one page:
        try:
            pages = await self.catch.text(soup.select(self.scrape['pages'])[-1])
        except IndexError:
            pages = '1'
        
        # the current pages returns "Previous" instead of number, this only happens there only two pages, that's why I have returned the value 2.
        try: 
            return int(pages)  
        except ValueError:
            return 2
    
    
    async def split_url(self, url):  
        """
        Splits a given Amazon URL into multiple URLs, with each URL pointing to a different page of search results.
        
        Args:
            -url (str): The Amazon URL to be split.
        
        Returns:
            -list: A list of URLs, with each URL pointing to a different page of search results.
        """      
        
        # Create a list to store the split URLs, and add the original URL to it.
        split_url = [url]          
        
        # Use the 'num_of_pages' method to get the total number of search result pages for the given URL.
        total_pages = await self.num_of_pages(url)  
        
        print(f"Total number of pages || {str(total_pages)}.")        
         
        # Use the 'static_connection' method to make a static connection to the given URL and get its HTMl content.         
        content = await self.static_connection(url)
        
        # Making a soup:
        soup = BeautifulSoup(content, 'lxml')
        
        # Get the URL of the next button on the search result page and construct the URL of the next search result page.
        next_link = f"""https://www.amazon.com{await self.catch.attributes(soup.select_one(self.scrape['next_button']), 'href')}"""            
        
        # Loop through all the search result pages and construct a URL for each page.
        for num in range(1, total_pages):
            # Replace the page number in the URL with current page number increment by 1.
            next_url = re.sub(r'page=\d+', f'page={num+1}' , next_link)
            
            # Replace the 'sr_pg_' parameter in the URL with the current page number.
            next_url = re.sub(r'sr_pg_\d+', f'sr_pg_{num}', next_url)
            
            split_url.append(next_url)
        
        return split_url   
    

    async def getASIN(self, url):
        """
        Extracts the ASIN (Amazon Standard Identification Number) from the given URL.
        
        Args:
            url (str): The URL to extract the ASIN from.
        
        Return:
            str: The ASIN extracted from the URL.
        
        Raises:
            IndexError: If the ASIN cannot be extracted from the URL.
        """
        try:
            # If the URL contains 'dp', extract the ASIN from the second element of the list obtained by splitting the URL by 'dp'.
            split_url = url.split('dp')[-1].split('/')[1]
        except IndexError:
            # If indexerror as there may vary in links structure, extract the ASIN from the first element of the list obtained by splitting the URL by 'dp' and then by '?'.
            split_url = url.split('dp')[1].split("?")[0].replace("/", "")
            
        return split_url              

  
    async def amazonMe(self, interval, urls):
        """
        Scrapes data from multiple pages of an Amazon search result for a given interval of time and saves the data into an Excel file.
        
        Args:
            -interval (int): The time interval between each page request in seconds.
            -urls (list): Alist of URLs to scrape data from.
        
        Returns:
            -str: A message indicating the success of the scraping and saving operation.
            
        Raises:
            -Exception: If there is an error loading the content from Amazon or extracting data from the HTML.
        """
        amazon_dicts = []
        
        # Verify if the first URL is a valid Amazon link:
        if await verify_amazon(urls[0]):
            print("Invalid link. Please try proper amazon link product category of your choice.")
            return              
        
        # Get base content and soup from first URL:
        base_content = await self.static_connection(urls[0])  
        base_soup = BeautifulSoup(base_content, 'lxml')        
        
        # Get search results from first URL:
        try:
            search_results = re.sub(r"""["]""", "", base_soup.select_one(self.scrape['searches']).text.strip()).title()
        except AttributeError:
            search_results = base_soup.select_one('span.a-list-item').text.strip()
        
        # Check if main content element exists on page:
        try:
            base_soup.select_one(self.scrape['main_content'])
        except Exception as e:
            return f"Content loading error. Please try again in few minutes. Error message: {e}"        
        
        # Loop through all the URLs and scrape data from each page:
        for pages in range(len(urls)):
            print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"Scraping pages || {pages + 1}")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            
            # Wait for random interval before making next request
            await asyncio.sleep(randomTime(interval)) 
            
            # Get content and soup from current URL:
            content = await self.static_connection(urls[pages])
            soup = BeautifulSoup(content, 'lxml')
            
            # Get product card contents from current page:         
            card_contents = soup.select(self.scrape['main_content'])
            
            # Loop through all product cards and extract data:            
            for datas in card_contents:
                prod_hyperlink = f"""https://www.amazon.com{await self.catch.attributes(datas.select_one(self.scrape['hyperlink']), 'href')}"""
                prod_name = await self.catch.text(datas.select_one(self.scrape['hyperlink']))
                print(prod_name)
                data = {
                    'Product': prod_name,
                    'ASIN': await self.getASIN(prod_hyperlink),
                    'Price': await self.catch.text(datas.select_one(self.scrape['price'])),
                    'Original price': await self.catch.text(datas.select_one(self.scrape['old_price'])),
                    'Review': await self.catch.text(datas.select_one(self.scrape['review'])),
                    'Review count': await self.catch.text(soup.select_one(self.scrape['review_count'])),
                    'Hyperlink': prod_hyperlink,
                    'Image url': f"""{await self.catch.attributes(datas.select_one(self.scrape['image']), 'src')}""",
                }
                amazon_dicts.append(data)       
        
        # Create directory to save Excel file:
        directory_name = 'Amazon database'
        await create_path(directory_name)

        # Save data to Excel file:
        df = pd.DataFrame(amazon_dicts)
        df.to_excel(f"{os.getcwd()}//Amazon database//{search_results}-Amazon database.xlsx", index=False)
        print(f"{search_results} is saved.")


    async def dataByAsin(self, asin):
        """
        Extracts product information from the Amazon product page by ASIN (Amazon Standard Identification Number).
        
        Args:
            -asin (str): The ASIN of the product to extract informatio from.
        
        Returns:
            -dict: A dictionary containing product information, including name, price, rating, rating count, availability,
                   hyperlink, image link, store, and store link.
        
        Raises:
            -AttributeError: If the product information cannot be extracted from the page.
        """
        
        # Construct the URL using the ASIN:
        url = f"https://www.amazon.com/dp/{asin}"
        
        # Retrieve the page content using 'static_connection' method:
        content = await self.static_connection(url)       
        soup = BeautifulSoup(content, 'lxml')
        
        try:
            # Try to extract the image link using the second first selector.
            image_link = soup.select_one(self.scrape['image_link_I']).get('src')
        except AttributeError:
            try:
                # If images not found in first selector, try second selector:
                image_link = soup.select_one(self.scrape['image_link_II']).get('src')
            except AttributeError:
                # If the image link cannot be extracted, return an error message:
                return 'Content loading error. Please try again in few minutes.'        
        
        try:
            availabilities = soup.select_one(self.scrape['availability']).text.strip()
        except AttributeError:
            availabilities = 'In stock'
            
        store = await self.catch.text(soup.select_one(self.scrape['store']))
        store_link = f"""https://www.amazon.com{await self.catch.attributes(soup.select_one(self.scrape['store']), 'href')}"""
        
        # Construct the data dictionary containing product information:
        datas = {
            'Name': await self.catch.text(soup.select_one(self.scrape['name'])),
            'Price': await self.catch.text(soup.select_one(self.scrape['price_us'])),
            'Rating': await self.catch.text(soup.select_one(self.scrape['review'])),
            'Rating count': await self.catch.text(soup.select_one(self.scrape['rating_count'])),
            'Availability': availabilities,
            'Hyperlink': url,
            'Image': image_link,
            'Store': store,
            'Store link': store_link,

        }                
        
        return datas
                
        