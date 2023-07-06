from tools.tool import flat, export_sheet
from scrapers.scraper import Amazon
import pymongo as mong


async def export_to_mong(url):
    amazon = Amazon()
    client = mong.MongoClient("mongodb://localhost:27017/")
    db = client['amazon']
    collection_name = await amazon.category_name(url)
    print(f"Collecting {collection_name} to Mongo database.")
    collection = db[collection_name]
    datas = await amazon.concurrent_scraping(url)
    result = collection.insert_many(flat(datas))
    client.close()
    return result


async def mongo_to_sheet(coll_name):
    client = mong.MongoClient('mongodb://localhost:27017')
    db = client['amazon']
    collection_category = db[coll_name]
    datas = list(collection_category.find({}))
    await export_sheet(datas, coll_name)
    client.close()


async def data_by_asin(asin):
    client = mong.MongoClient("mongodb://localhost:27017/")
    db = client['amazon']
    collection = db['playstation_5_accessories']
    query = {"ASIN": asin}
    filtered_doc = [doc for doc in collection.find(query)]
    client.close()
    return filtered_doc

