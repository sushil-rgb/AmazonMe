from tools.tool import flat, export_sheet
from scrapers.scraper import Amazon
import pymongo as mong


async def export_to_mong(url, proxy):
    """
    Scrapes product information from Amazon and exports it to a MongoDB database.

    Args:
        - url (str): The Amazon URL to scrape data from.
        - proxy (str): The proxy to use for the request.

    Returns:
        - pymongo.results.InsertManyResult: The result of the insertion into the MongoDB collection.
    """# Create an instance of the Amazon class with the provided URL and proxy:
    amazon = Amazon(url, proxy)

    # Connect to the MongoDB database:
    client = mong.MongoClient("mongodb://localhost:27017/")
    db = client['amazon']

    # Get the collection name based on the category name:
    collection_name = await amazon.category_name()

    # Print a message about collecting data to the Mongo database:
    print(f"Collecting {collection_name} to Mongo database.")

    # Access or create the collection in the MongoDB database:
    collection = db[collection_name]

    # Scrape and save product information concurrently:
    datas = await amazon.concurrent_scraping()

    # Insert the scraped data into the MongoDB collection:
    result = collection.insert_many(flat(datas))

    # Close the MongoDB connection:
    client.close()
    return result


async def mongo_to_sheet(coll_name):
    """
    Retrieves data from a MongoDB collection and exports it to an Excel sheet.

    Args:
        - coll_name (str): The name of the MongoDB collection to retrieve data from.

    Returns:
        - None
    """
    # Connect to the MongoDB database:
    client = mong.MongoClient('mongodb://localhost:27017')
    db = client['amazon']

    # Access the specified collection in the MongoDB database:
    collection_category = db[coll_name]

    # Retrieve all documents from the collection:
    datas = list(collection_category.find({}))

     # Export the data to an Excel sheet:
    await export_sheet(datas, coll_name)

    # Close the MongoDB connection:
    client.close()


async def data_by_asin(asin):
    client = mong.MongoClient("mongodb://localhost:27017/")
    db = client['amazon']
    collection = db['playstation_5_accessories']
    query = {"ASIN": asin}
    filtered_doc = [doc for doc in collection.find(query)]
    client.close()
    return filtered_doc

