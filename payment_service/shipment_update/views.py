# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from payment.models import payment_status as paystat
import requests
import json


def shipment_details_update(uname):
    ship_dict = {}
    
    # Get data from payment info.
    user = paystat.objects.filter(username=uname)
    for data in user.values():
        data
        ship_dict['product_id'] = data['product_id']
        ship_dict['quantity'] = data['quantity']
        ship_dict['payment_status'] = data['status']
        ship_dict['transaction_id'] = data['id']
        ship_dict['mobile_number'] = data['mobile']
        
    # Get the user info.
    url = 'http://192.168.52.131:3001/userinfo/'
    d1 = {}
    d1["username"] = data['username']
    data = json.dumps(d1)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    val1 = json.loads(response.content.decode('utf-8'))
    print(val1)
    ship_dict['first_name'] = val1['data']['first_name']
    ship_dict['last_name'] = val1['data']['last_name']
    ship_dict['address'] = val1['data']['address']
    ship_dict['email_id'] = val1['data']['email_id']
    # Call the shipment_updates API.
    url = 'http://192.168.52.131:3004/shipment_updates/'
    data = json.dumps(ship_dict)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=data, headers=headers)
    api_resp = json.loads(response.content.decode('utf-8'))
    print(api_resp)
    return api_resp
