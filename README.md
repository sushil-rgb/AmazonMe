# Amazon Scraper Apify Actor

This Apify actor is a web scraper specifically built for extracting product information from Amazon based on category URLs. It utilizes Apify's powerful web scraping capabilities and Python to collect detailed product data for analysis, research, or any other purpose.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Input](#input)
- [Output](#output)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Apify actor navigates through specified Amazon category URLs, extracts product details such as title, price, description, and reviews, and stores the data in a structured JSON format. It provides a seamless way to collect Amazon product information for various use cases.

## Usage

To use this Amazon scraper, simply input the category URLs for the products you want to scrape. The actor will navigate through the specified categories, extract product details such as title, price, description, and reviews, and store the data in a structured format.

**Usage Example:**
1. Input the Amazon category URLs into the actor.
2. Run the actor.
3. Retrieve the scraped product data in the desired output format.

## Input

**Input Parameters:**
- `categoryUrls` (Strings): A string Amazon category URLs that you want to scrape.
  - Example: `"https://www.amazon.it/s?rh=n%3A10815246031&fs=true&ref=lp_10815246031_sar"`

## Output

**Output Format:**
The scraper outputs data in a structured JSON format, including the following fields for each product:
- `title`: Product title.
- `asin`: Product ASIN.
- `description`: Product description.
- `price`: Product price.
- `youSaved`: Product saved price.
- `reviews`: Product reviews, ratings and counts.
- `availability`: Product availability,
- `hyperlink`: Product URL,
- `imageLink`: Product thumbnail URL,
- `images`: Products thumbnail URL in lists,
- `store`: Product store name,
- `storeLink`: Product store URL,


Example Output:
```json
{
  "products": [
    {
      "name": "Skullcandy Jib True 2 In-Ear Wireless Earbuds, 32 Hr Battery, Microphone, Works with iPhone Android and Bluetooth Devices - Black",
      "asin": "B09VM2TBZF",
      "description": "Never Lost with Tile - Tile tech makes it easy to track down either earbuds if you ever misplace one. Just download the Tile app and simply 'ring' for your buds. Use Either Bud Solo - Jib True 2 features solo mode, which enables you to use either earbuds separately to take calls or listen to music. Enjoy Fearlessly - With an IPX4 rating, Jib True 2 can handle a little rain during your outdoor adventure. 33 Hours of Power - With Jib True 2, you can experience longer-lasting listening sessions without worry. Enjoy wireless freedom with 24 hours of power in the case and 9 hours in the earbuds. Buy with Confidence - 1 year US warranty included.
      ",
      "price": "$29.95",
      "dealPrice": "N/A",
      "youSaved": "N/A",
      "reviews": {
        "rating": 4.3,
        "count": 2286
      },
      "availability": "In Stock",
      "Hyperlink": "https://www.amazon.com/Skullcandy-True-Wireless-Ear-Earbuds/dp/B09VM2TBZF",
      "imageLink": "https://m.media-amazon.com/images/I/61h5ALBhEtL.__AC_SX300_SY300_QL70_ML2_.jpg",
      "Images": ["https://m.media-amazon.com/images/I/318ZX1G-ZmL._AC_US40_.jpg", "https://m.media-amazon.com/images/I/31jlRyzHkZL._AC_US40_.jpg", "https://m.media-amazon.com/images/I/312lsbggTQL._AC_US40_.jpg", "https://m.media-amazon.com/images/I/419SPoM3U3L._AC_US40_.jpg", "https://m.media-amazon.com/images/I/41DKKeaOe6L._AC_US40_.jpg", "https://m.media-amazon.com/images/I/41D7WcHT+AL._AC_US40_.jpg", "https://m.media-amazon.com/images/I/41Q97yInqUL.SS40_BG85,85,85_BR-120_PKdp-play-icon-overlay__.jpg", "https://images-na.ssl-images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V192234675_.gif"],
      "Store": "Skullcandy Store",
      "Store link": "https://www.amazon.com/stores/Skullcandy/page/9F16B940-F912-43FE-888C-5BB1B86337A9?ref_=ast_bln",
    }
  ]
}
```

## Supported domains:
- <b>".com"</b>          (US)
- <b>".co.uk"</b>        (UK)
- <b>".com.mx"</b>       (Mexico)
- <b>".com.br"</b>       (Brazil)
- <b>".com.au"</b>       (Australia)
- <b>".com.jp"</b>       (Japan)
- <b>".com.be"</b>       (Belgium)
- <b>".in"</b>           (India)
- <b>".fr"</b>           (France)
- <b>".se"</b>           (Sweden)
- <b>".de"</b>           (Germany)
- <b>".it"</b>           (Italy)

**Configuration Options:**
- None at the moment. The actor is configured to scrape product data from the provided category URLs.


**Development:**
- **Installation:** Clone the repository and install the necessary dependencies using `pip install -r requirements.txt`.
- **Usage:** Run the actor locally using `npm start` and test with different category URLs.


**Contributing:**
- If you find any issues or have suggestions, please open an issue on GitHub.
- Contributions are welcome! Fork the repository, create a branch, make changes, and open a pull request.
- Follow the ESLint rules and maintain clean code standards.


**License:**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


