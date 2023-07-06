from tools.tool import flat, export_sheet
from scrapers.scraper import Amazon
import pymongo as mong
import pandas as pd


async def export_to_mong(url):    
    amazon = Amazon() 
    client = mong.MongoClient("mongodb://localhost:27017/")
    db = client['amazon']
    collection_name = await amazon.category_name(url)
    print(f"Collecting {collection_name} to Mongo database.")
    collection = db[collection_name]
    datas = await amazon.concurrent_scraping(url)
    
    result = collection.insert_many(flat(datas))
    # print("Inserted IDs:", result.inserted_ids)
    client.close()
    return result


async def mongo_to_sheet(coll_name):
    client = mong.MongoClient('mongodb://localhost:27017')
    db = client['amazon']
    collection_category = db[coll_name]
    datas = list(collection_category.find({}))
    await export_sheet(datas, coll_name)
    # df = pd.DataFrame(datas)
    # df.to_excel(f"{coll_name}.xlsx", index = False)


async def data_by_asin(asin):
    client = mong.MongoClient("mongodb://localhost:27017/")
    db = client['amazon']
    collection = db['playstation_5_accessories']
    # return collection.find()

    # asin = "B07DLKVKD5"
    query = {"ASIN": asin}
    filtered_doc = [doc for doc in collection.find(query)]
    return filtered_doc



# print(asyncio.run(data_by_asin("B09JFFX786")))
# print(asyncio.run(export_to_mong()))
# print(asyncio.run(export_to_sheet()))
    



