from django.http import HttpResponse
from . import models

def myview(request):
    objs = models.MyModel.objects.all()
    num = len(objs)
    return HttpResponse(f'Hello: {num}')

