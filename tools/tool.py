import pandas as pd
import itertools
import asyncio
import aiohttp
import secrets
import yaml
import re
import os


class Response:
    def __init__(self, base_url):
        self.base_url = base_url

    async def content(self):
        async with aiohttp.ClientSession() as session:
            headers = {'User-Agent': userAgents()}
            async with session.get(self.base_url, headers = headers) as resp:
                cont = await resp.read()
                return cont

    async def response(self):
        async with aiohttp.ClientSession() as session:
            headers = {'User-Agent': userAgents()}
            async with session.get(self.base_url, headers = headers) as resp:
                cont = resp.status
                return cont


def filter(raw_lists):
    filtered_lists = []
    for file in raw_lists:
        if not file in filtered_lists:
            filtered_lists.append(file)
    return filtered_lists


def flat(d_lists):
    """
    Flatten a multi-dimentional list.

    Args:
    - d_lists (list): A multi-dimensional list.

    Returns:
    - list: A flattened version of the input list.
    """
    return list(itertools.chain(*d_lists))


async def static_connection(url, proxy):
    proxy_username = "xtusztej"
    proxy_password = "bx2x4u4oemm6"
    auth = aiohttp.BasicAuth(proxy_username, proxy_password)
    connector = aiohttp.TCPConnector(ssl = False)

    async with aiohttp.ClientSession(connector = connector) as session:
        async with session.get(url,
                            headers={'User-Agent': userAgents()},
                            proxy = proxy,
                            proxy_auth = auth,
                            ) as resp:
            content = await resp.read()
        return content


async def verify_amazon(url):
    """
    Verifies if the input URL is a vaild Amazon URL.

    Args:
        -url: A string representing the URL to verify.

    Returns:
        -True if the URL is invalid or False if it is valud.
    """
    amazon_pattern = re.search("""^(https://|www.)|amazon\.(com|co\.uk)(/s\?.|/b/.)+""", url)
    if amazon_pattern == None:
        return True
    else:
        pass


async def export_sheet(dicts, name):
    """
    Exports a list of dictinaries to an Excel file with the specified name and saves it to a directory called 'Amazon database':

    Args:
        -dicts (List[Dict]): A list of dictionaries to export to an Excel file.
        -name (str): The name to use for the Excel file (without the file extension).

    Returns:
        -None
    """
    directory_name = 'Amazon database'
    await create_path(directory_name)
    df = pd.DataFrame(dicts)
    df.to_excel(f"""{os.getcwd()}//{directory_name}//{name}-Amazon database.xlsx""", index = False)
    print(f"{name} saved.")


def random_values(d_lists):
    """
    Returns a random value from a list.

    Args
    """
    idx = secrets.randbelow(len(d_lists))
    return d_lists[idx]


async def create_path(dir_name):
    """
    Creates a directory with the specified name if i doesn't already exist.

    Args:
        -dir_name: A string representing the name of the direcory to create.

    Return:
        -None
    """
    path_dir = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(path_dir):
        pass
    else:
        os.mkdir(path_dir)


async def randomTime(val):
    """
    Generates a random time interval between requests to avaoid overloading the server. Scrape resonponsibly.

    Args:
        -val: An interger representing the maxinum time interval in seconds.

    Returns:
        -A random interger between 2 and the input value. So, the default time interval is 2 seconds.
    """
    ranges = [i for i in range(0, val+1)]
    return random_values(ranges)


def userAgents():
    """
    Returns a random user agent string from a file containing a list of user agents.

    Args:
        -None

    Returns:
        -A string representing a ranom user agent.
    """
    with open('tools//user-agents.txt') as f:
        agents = f.read().split("\n")
        return random_values(agents)


def rand_proxies():
    with open('proxies.txt') as f:
        proxies = f.read().split("\n")
        return random_values(proxies)


def yaml_load(selectors):
    """
    Loads a YAML file containing selectors for web scraping.

    Args:
        -selectors: A string representing the name of the YAML file containing the selectors.

    Returns:
        -A dictionary containing the selectors.
    """
    with open(f"scrapers//{selectors}.yaml") as file:
        sel = yaml.load(file, Loader=yaml.SafeLoader)
        return sel


class TryExcept:
    """
    A class containing methord for seafely extracting information from HTML elements.
    """
    async def text(self, element):
        """
        Returns the text content of an HTML element, or "N/A" if the element is not found.

        Args:
            -element: An HTML element object.

        Returns:
            -A string representing the text content of the elemen, or "N/A" if the element is not found.
        """
        try:
            elements = element.text.strip()
        except AttributeError:
            elements = "N/A"
        return elements

    async def attributes(self, element, attr):
        """
        Returns the value fo an attribute of an HTML element, of "N/A" if the attribute or element is not found.

        Args:
            -element: An HTML element object.
            -attr: A string representing the name of the attribute to extract.

        Returns:
             A string representing the value of the attribute, or "N/A" if the attribute or element is not found.
        """
        try:
            elements = element.get(attr)
        except AttributeError:
            elements = "N/A"
        return elements

