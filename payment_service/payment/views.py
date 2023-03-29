# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from payment.models import payment_status as paystat
from shipment_update.views import shipment_details_update as ship_update

def get_transaction_details(uname):
    user = paystat.objects.filter(username=uname)
    for data in user.values():
        return data

def store_data(uname, prodid, price, quantity, mode_of_payment, mobile):
    user_data = paystat(username=uname, product_id=prodid, price=price, quantity=quantity, 
                        mode_of_payment=mode_of_payment, mobile=mobile, status="Success")
    user_data.save()
    return 1

@csrf_exempt
def get_payment(request):
    data = json.loads(request.body)
    uname = data.get("user_name")
    prodid = data.get("product_id")
    price = data.get("price")
    quantity = data.get("quantity")
    mode_of_payment = data.get("payment_mode")
    mobile = data.get("mobile_number")
    resp = {}
    if uname and prodid and price and quantity and mode_of_payment and mobile:
        respdata = store_data(uname, prodid, price, quantity, mode_of_payment, mobile)
        respdata2 = ship_update(uname)
        if respdata:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Transaction is completed.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Transaction is failed, Please try again.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'All fields are mandatory.'
    return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def user_transaction_info(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            uname = val1.get('user_name')
            resp = {}
            if uname:
                respdata = get_transaction_details(uname)
                if respdata:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = respdata
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')
