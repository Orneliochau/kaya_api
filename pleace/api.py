from ninja import NinjaAPI
from pleace.schema import PleaceSchema, EmployeeIn
from pleace.models import PleaceInformation, Employee, department_id
from django.core.files.storage import FileSystemStorage
from ninja import UploadedFile, File



api = NinjaAPI()

@api.post('/places')
def PlaceApi(request, payload:PleaceSchema):
    place_obj = PleaceInformation.objects.create(**payload.dict())
    return {"place_name": place_obj.place_name}

@api.get('/home')
def homeView(request):
    return {"Message":"Hello guys"}

@api.post('/employee')
def create_employee(request, payload:EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {'id': employee.id}

STORAGE = FileSystemStorage()

@api.post('upload/')
def create_upload(request, cv:UploadedFile=File(...)):
    filename = STORAGE.save(cv.name, cv)
