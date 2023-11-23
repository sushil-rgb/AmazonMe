from scrapers.scraper import Amazon


async def get_category_offer(category_name):
    categ_url = f"https://www.amazon.it/s?k=offerte+{category_name}"
    offers = await Amazon(categ_url, None).export_csv()
    return offers

