# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user_model.models import user_registration

def user_validation(uname, password):
    user_data = user_registration.objects.filter(email=uname, password=password)
    if user_data:
        return "Valid User"
    else:
        return "Invalid User"

@csrf_exempt
def user_login(request):
    data = json.loads(request.body)
    uname = data.get("username")
    password = data.get("password")
    resp = {}
    if uname and password:
        respdata = user_validation(uname, password)
        if respdata == "Valid User":
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Welcome to Ecommerce website......'
        elif respdata == "Invalid User":
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Invalid credentials.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')
