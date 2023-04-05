# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    type = models.CharField(max_length=100, default='book')
    created_at = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s %s %s' % (self.user_id, self.product_id, self.quantity, self.created_at, self.status)

    def release(cart):
        b = {}
        b['id'] = cart.get('id', '')
        b['user_id'] = cart.get('user_id', '')
        b['product_id'] = cart.get('product_id', '')
        b['quantity'] = cart.get('quantity', '')
        b['created_at'] = cart.get('created_at', '')
        b['status'] = cart.get('status', '')
        return b
