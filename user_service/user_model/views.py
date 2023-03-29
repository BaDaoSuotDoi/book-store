# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration
def data_insert(fname, lname, email, mobile, password, address):

  user_data = user_registration(
    fname=fname, lname=lname, email=email, mobile=mobile, password=password, address=address)
  user_data.save()
  return 1


@csrf_exempt
def registration_req(request):

  data =  json.loads(request.body)
  fname = data.get("first_name")
  print(fname)
  lname = data.get("last_name")
  email = data.get("email")
  mobile = data.get("mobile_number")
  password = data.get("password")
  cnf_password = data.get("confirm_password")
  address = data.get("address")
  resp = {}
  if fname and lname and email and mobile and password and cnf_password and address:
    if len(str(mobile)) == 10:
      if password == cnf_password:
        respdata = data_insert(fname, lname, email, mobile,
                        password, address)
        if respdata:
          resp['status'] = 'Success'
          resp['status_code'] = '200'
          resp['message'] = 'User is registered Successfully.'
        else:
          resp['status'] = 'Failed'
          resp['status_code'] = '400'
          resp['message'] = 'Unable to register user, Please try again.'
      else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Password and Confirm Password should be same.'
    else:
      resp['status'] = 'Failed'
      resp['status_code'] = '400'
      resp['message'] = 'Mobile Number should be 10 digit.'
  else:
    resp['status'] = 'Failed'
    resp['status_code'] = '400'
    resp['message'] = 'All fields are mandatory.'
  return HttpResponse(json.dumps(resp), content_type= 'application/json')
