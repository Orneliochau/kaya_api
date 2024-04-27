"""
for more information https://django-ninja.dev/guides/input/body/ 

Request Body
Request bodies are typically used with “create” and “update” operations (POST, PUT, PATCH). For example, when creating a resource using POST or PUT, the request body usually contains the representation of the resource to be created.

To declare a request body, you need to use Django Ninja Schema.

Info

Under the hood Django Ninja uses Pydantic models with all their power and benefits. The alias Schema was chosen to avoid confusion in code when using Django models, as Pydantic's model class is called Model by default, and conflicts with Django's Model class.

Import Schema
First, you need to import Schema from ninja:

from typing import Optional
from ninja import Schema


class Item(Schema):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


"""





from ninja import Schema

class PleaceSchema(Schema):
    place_name: str
    description: str
    location: str
    price: float
    is_active: bool

