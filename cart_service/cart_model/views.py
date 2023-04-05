from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models.cart import Cart
import requests
import json

@csrf_exempt
def get_list_cart(request):
    status = request.GET["status"]
    print(status)
    carts = Cart.objects.filter(status=status)
    _carts = []
    for cart in carts.values() :
        _carts.append(Cart.release(cart))
    resq = {}
    resq['status'] = True
    resq['carts'] = _carts
    return HttpResponse(json.dumps(resq), content_type='application/text')

@csrf_exempt
def create(request):
    data = json.loads(request.body)
    product_id = data.get('product_id', '')
    quantity = data.get('quantity', '')
    type = data.get('type', '')
    cart = Cart(
        user_id = data.get('user_id', ''),
        product_id = product_id,
        quantity = quantity,
        type = type,
        created_at = data.get('created_at', ''),
        status = 'wait'
    )
    cart.save()
    ship_dict={}
    ship_dict['product_id'] = product_id
    ship_dict['quantity'] = quantity
    data = json.dumps(ship_dict)
    headers = {'Content-Type': 'application/json'}
    requests.post('http://10.1.48.35:3002/book/update/quantity', data=data, headers=headers)
    
    resq = {}
    resq['status'] = True
    resq['message'] = 'Update cart successful'
    return HttpResponse(json.dumps(resq), content_type='application/text')


@csrf_exempt
def update_status(request):
    data = json.loads(request.body)
    id = data.get('id', '')
    status = data.get('status', '')
    cart = Cart.objects.get(id=id)
    cart.status = status
    cart.save()
    resq = {}
    resq['status'] = True
    resq['message'] = 'Update status cart successful'
    return HttpResponse(json.dumps(resq), content_type='application/text')
