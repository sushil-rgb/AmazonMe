from pydantic import BaseModel, Field


class AamazonRecord(BaseModel):
    """
    A Pydantic BaseModel to represent Amazon product's records.
    
    Attributes:
    -----------
    ASIN : str
        -The unique Amazon Standard Identification Number of the product.
    Name: str
        -The name of the product.
    Price: str
        -The price of the product.
    Rating: str
        -The rating of the product.
    Rating_count: str
        -The number of rating the product has.
    Availability : str
        -The availability status of the product.
    Hyperlink: str
        -The hyperlink of the product on Amazon.
    Store: str
        -The name of the store selling the product.
    Store_link : str
        -The URL of the store selling the product.

    """
    ASIN: str = Field(..., alias = "ASIN")
    Name: str = Field(..., alias = "Name")
    Price: str = Field(..., alias = "Price")
    Rating: str = Field(..., alias = "Rating")
    Rating_count: str = Field(..., alias = "Rating count")
    Availability: str = Field(..., alias = "Availability")
    Hyperlink: str = Field(..., alias = "Hyperlink")
    Image: str = Field(..., alias = "Image")
    Store: str = Field(..., alias = "Store")
    Store_link: str = Field(..., alias = "Store link")

