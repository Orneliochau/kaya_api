from ninja import NinjaAPI
from pleace.schema import PleaceSchema
from pleace.models import PleaceInformation

api = NinjaAPI()

@api.post('/places')
def PlaceApi(request, payload:PleaceSchema):
    place_obj = PleaceInformation.objects.create(**payload.dict())
    return {"place_name": place_obj.place_name}

@api.get('/home')
def homeView(request):
    return {"Message":"Fuck you everyone"}
