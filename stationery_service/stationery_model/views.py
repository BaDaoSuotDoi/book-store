from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models.stationery import Stationery
from django.forms.models import model_to_dict

@csrf_exempt
def get_list_stationery(request):
    resp = {}
    stationeries = Stationery.objects.all()
    temp = []
    for stationery in stationeries.values() :
        temp.append(Stationery.release(stationery))

    resp['stationeries'] = temp
    return HttpResponse(json.dumps(resp), content_type='application/json')

