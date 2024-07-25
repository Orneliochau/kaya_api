from typing import Optional

from ninja import Schema
from datetime import date
 

class PleaceSchema(Schema):
    user_id: Optional[int]
    place_name: str
    description: str
    province: str
    city: str
    street_adress: str
    price: float
    facebook: str
    instagram: str

    

