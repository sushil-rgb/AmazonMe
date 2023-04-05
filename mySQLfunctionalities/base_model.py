import os
import mysql.connector
from pydantic import BaseModel, Field


class IPORecord(BaseModel):
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

