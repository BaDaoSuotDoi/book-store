# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ship_status.models import shipment as ship_obj

def ship_data_insert(fname, lname, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status):
    """This function is inserting the data into our table."""
    shipment_data = ship_obj(
        fname=fname,
        lname=lname,
        email=email,
        mobile=mobile,
        address=address,
        product_id=product_id,
        quantity=quantity,
        payment_status=payment_status,
        transaction_id=transaction_id,
        shipment_status=shipment_status
    )
    shipment_data.save()
    return 1

@csrf_exempt
def shipment_reg_update(request):
    """This function will get the data from the front end."""
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            fname = val1.get("first_name")
            lname = val1.get("last_name")
            email = val1.get("email_id")
            mobile = val1.get("mobile_number")
            address = val1.get("address")
            product_id = val1.get("product_id")
            quantity = val1.get("quantity")
            payment_status = val1.get("payment_status")
            transaction_id = val1.get("transaction_id")
            shipment_status = "ready to dispatch"
            resp = {}
            respdata = ship_data_insert(
                fname, lname, email, mobile, address, product_id, quantity,
                payment_status, transaction_id, shipment_status
            )
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Product is ready to dispatch.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Failed to update shipment details.'
            return HttpResponse(json.dumps(resp), content_type='application/json')

def shipment_data(uname):
    """This function is used for finding the transaction."""
    data = ship_obj.objects.filter(email=uname)
    for val in data.values():
        return val

@csrf_exempt
def shipment_status(request):
    """This function is used for getting the shipment status."""
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            uname = variable1.get("User Name")
            resp = {}
            respdata = shipment_data(uname)
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User data is not available.'
            return HttpResponse(json.dumps(resp), content_type='application/json')
