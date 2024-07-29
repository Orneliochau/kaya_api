from ninja import NinjaAPI
from place.schema import PleaceSchema
from place.models import PleaceInformation, placeImages
from ninja import UploadedFile, File
from django.http import JsonResponse
from django.forms.models import model_to_dict
from ninja.errors import HttpError


api = NinjaAPI()

@api.post('create/place')
def PlaceApi(request, payload:PleaceSchema):
    place_obj = PleaceInformation.objects.create(**payload.dict())
    return JsonResponse({
        'name': place_obj.place_name,
        'description': place_obj.description,
        'province': place_obj.province,
        'street_adress': place_obj.street_adress,
        'price': place_obj.price,
        'facebook': place_obj.facebook,
        'instagram': place_obj.instagram

    })

@api.get('places')
def get_all_places(request):
    places = PleaceInformation.objects.all()
    response = [{'id':place.id,'name': place.place_name,'description': place.description,'province': place.province,'street_adress': place.street_adress,'price': place.price,'facebook': place.facebook,'instagram': place.instagram} for place in places]
    return response

@api.get('place/{place_id}')
def get_place_by_id(request, place_id:int):
    try:
        place = PleaceInformation.objects.get(id=place_id)
        return place
    except PleaceInformation.DoesNotExist:
        raise HttpError(404, 'Place not found')
    
@api.get('place')
def get_place_by_user(request):
    user = request.user
    places = PleaceInformation.objects.filter(user=user)
    response = [{'id':place.id,'name': place.place_name,'description': place.description,'province': place.province,'street_adress': place.street_adress,'price': place.price,'facebook': place.facebook,'instagram': place.instagram} for place in places]
    return response

@api.put('update/place/{place_id}')
def update_place(request, data:PleaceSchema, place_id:int):
    try:
        place = PleaceInformation.objects.get(id=place_id)
        place.place_name = data.place_name
        place.description = data.description
        place.province = data.province
        place.city = data.city
        place.street_adress = data.street_adress
        place.price = data.price
        place.facebook = data.facebook
        place.instagram = data.instagram
        place.save()
        return place
    except PleaceInformation.DoesNotExist:
        raise HttpError(404, 'Place not found')
    
@api.delete('delete/place/{place_id}')
def delete_place(request, place_id:int):
    try:
        place = PleaceInformation.objects.get(id=place_id)
        place.delete()
        return {'Delete': True}
    except PleaceInformation.DoesNotExist:
        raise HttpError(404, 'Place not found')

@api.post('upload/images')
def upload_images(request, place_id:int, front:File[UploadedFile], back:File[UploadedFile], left:File[UploadedFile], right:File[UploadedFile]):
    place = PleaceInformation.objects.get(id=place_id)
    images = placeImages.objects.create(
        place = place,
        front = front,
        back = back,
        left = left,
        right = right

    )
    images.save()
    print(images)
    return images

@api.put('update/images/{place_id}')
def update_images(request, place_id: int, front:UploadedFile = None, back: UploadedFile= None, left:UploadedFile=None, right:UploadedFile=None): 
    place = placeImages.objects.get(id=place_id)
    place.front = front
    place.back = back
    place.left = left
    place.right = right
    place.save()
    return place

@api.delete('delete/images/{place_id}')
def delete_images(request, place_id: int):
    try:
        place_images = placeImages.objects.get(id=place_id)
        place_images.delete()
        return {"Image":"Deleted"}
    except placeImages.DoesNotExist:
        raise HttpError(404, 'Images not found')

@api.get('images')
def get_all_images(request):
    try:
        images = placeImages.objects.all()
        return images
    except placeImages.DoesNotExist:
        raise HttpError(404, 'Not found images')

@api.get('image/{place_id}')
def get_image_by_id(request, place_id: int):
    try:
        image = placeImages.objects.get(id=place_id)
        return image
    except placeImages.DoesNotExist:
        raise HttpError(404, 'Not found images')
   
