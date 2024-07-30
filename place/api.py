from ninja import NinjaAPI
from place.schema import PleaceSchema
from place.models import PleaceInformation, placeImages
from ninja import UploadedFile, File

from ninja.errors import HttpError



api = NinjaAPI()

@api.post('create/place')
def PlaceApi(request, payload:PleaceSchema, profile_photo:File[UploadedFile]):
    return PleaceInformation.objects.create(**payload.dict())

@api.get('places')
def get_all_places(request):
    return PleaceInformation.objects.all()

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
    return PleaceInformation.objects.filter(user=user)

@api.put('update/place/{place_id}')
def update_place(request, data:PleaceSchema, place_id:int, profile_photo: UploadedFile =None):
    try:
        place = PleaceInformation.objects.get(id=place_id)
        place.profile_photo = profile_photo
        place.place_name = data.place_name
        place.description = data.description
        place.province = data.province
        place.city = data.city
        place.street_adress = data.street_adress
        place.price = data.price
        place.facebook = data.facebook
        place.instagram = data.instagram
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
   
