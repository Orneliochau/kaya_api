from ninja import Schema

class PleaceSchema(Schema):
    place_name: str
    description: str
    location: str
    price: float
    is_active: bool

