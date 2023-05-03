from functionalities.tools import TryExcept, yaml_load, randomTime, userAgents, verify_amazon, export_to_sheet
from bs4 import BeautifulSoup
import pandas as pd
import asyncio
import aiohttp
import re


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
        try:      
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers = self.headers) as resp:
                    content = await resp.read()
                    return content
        except Exception as e:
            return f"Content loading erro: URL |> {url} | Error |> {str(e)}."
    
    
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
        
        # Create a list to store the split URLs, and add the orignal URL to it:           
        split_url = [url]     
        
        # Use the 'num_of_pages' method to get the total number of search result pages for the given URL:                     
        total_pages = await self.num_of_pages(url)         
        
        # Use the 'static_connection' method to make a static connection to the given URL and get its HTML content:   
        content = await self.static_connection(url)        

        # Making a soup:
        soup = BeautifulSoup(content, 'lxml')        
        
        # Get the URL of the next button on the search result page and costruct the URL of the next search result page:
        next_link = f"""https://www.amazon.com{await self.catch.attributes(soup.select_one(self.scrape['next_button']), 'href')}"""     
        
        for num in range(1, total_pages):
            # Replace the 'page' number in the URL with curren tpage number increment by 1:            
            next_url = re.sub(r'page=\d+', f'page={num+1}' , next_link)            
            
            # Replace the 'sr_pg_' parameter in the URL with current page number:
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

    
    async def category_name(self, url):
        """
        Retrieves the category name of search results on the given Amazon search page URL.
        
        Args:
            -url (str): The Amazon search page URL to retrive category name.
            
        Raises:
            -None.
        """
        content = await self.static_connection(url)
        soup = BeautifulSoup(content, 'lxml') 
        try:       
            searches_results = (re.sub(r"""["]""", "", soup.select('span.a-color-state.a-text-bold')[-1].text.strip())).title()
        except IndexError:
        # if searches_results == 'Climate Pledge Friendly':
            searches_results = soup.select(self.scrape['searches_ii'])[1].text.strip()
        return searches_results                
            
    
    async def scrape_data(self, url):   
        """
        Scrapes product data from the Amazon search results page for the given URL.
        
        Args:
            -list: A list of dictionaries, with each dictionary containing product data for single product.
        
        Raises:
            -Expecation: If there is an error while loading the content of the Amazon search results page.
        """     
        amazon_dicts = []         
        
        # Use the 'static_connection' method to download the HTML content of the search results bage 
        content = await self.static_connection(url)  
        soup = BeautifulSoup(content, 'lxml')                     
        
        # Check if main content element exists on page:
        try:
            soup.select_one(self.scrape['main_content'])
        except Exception as e:
            return f"Content loading error. Please try again in few minutes. Error message: {e}"      
        
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
                'Review count': await self.catch.text(datas.select_one(self.scrape['review_count'])),                
                'Hyperlink': prod_hyperlink,
                'Image url': f"""{await self.catch.attributes(datas.select_one(self.scrape['image']), 'src')}""",
            }
            amazon_dicts.append(data)       
        
        return amazon_dicts

        
    async def scrape_and_save(self, interval, url):
        """
        Scrapes data from a given URL, saves it to a file, and returns the scarped data as a Pandas Dataframe.
        
        Args:
            -interval (int): Time interval in seconds to sleep before scraping the data.
            -url (str): The URL to scrape data from.
        
        Returns:
            -pd.DataFrame: A Pandas DataFrame containing the scraped data.
            
        Raises:
            -HTTPError: If the HTTP request to the URL returns an error status code.
            -Exception: If there is an error while scraping the data.
        """
        random_sleep = await randomTime(interval)
        await asyncio.sleep(random_sleep)
        datas = await self.scrape_data(url)
        return pd.DataFrame(datas)
    
        
    async def concurrent_scraping(self, interval, url):
        if await verify_amazon(url):
            return "I'm sorry, the link you provided is invalid. Could you please provide a valid Amazon link for the product category of your choice?"
        
        print(f"-----------------------Welcome to Amazon crawler---------------------------------")
        
        await asyncio.sleep(2)
        
        searches = await self.category_name(url)
        print(f"Scraping category || {searches}.")
        
        await asyncio.sleep(2)
        # Pull the number of pages of the category       
        number_pages = await self.num_of_pages(url)
        print(f"Total pages || {number_pages}.")
        
        await asyncio.sleep(2)        
        
        # Split the pagination and convert it list of urls
        url_lists = await self.split_url(url)        
        
        print(f"The extraction process has begun and is currently in progress. The web scraper is scanning through all the links and collecting relevant information. Please be patient while the data is being gathered.")
        coroutines = [self.scrape_and_save(interval, url) for url in url_lists]
        dfs = await asyncio.gather(*coroutines)
        results = pd.concat(dfs)
        
        await export_to_sheet(results, searches)
                   
    
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
                
        