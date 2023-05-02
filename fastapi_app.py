from scrapers.scraper import Amazon
from fastapi import FastAPI



url = "https://www.amazon.com/s?k=gaming+keyboard&pd_rd_r=623a9335-ce3a-4a2f-bbfc-15d5c97924b0&pd_rd_w=dXN1f&pd_rd_wg=gRRP9&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=SZQK6ZQZN2DH6WQEX2KE&ref=pd_gw_unk"
amazon = Amazon()

app = FastAPI()


@app.get("/test")
async def test_api():
    category_name = await amazon.category_name(url)
    urls = await amazon.split_url(url)
    test_data = await amazon.scrape_data(urls[1])
    return {
        f"""{category_name}""": test_data
    }