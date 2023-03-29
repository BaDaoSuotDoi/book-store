# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from product_model.models import product_details


@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}

    prodata = product_details.objects.all()

    for tbl_value in prodata.values():
        data.append(tbl_value)

    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'

    return HttpResponse(json.dumps(resp), content_type='application/json')
