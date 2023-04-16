# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class  Stationery(models.Model):
    name = models.CharField(max_length=100)
    availability = models.IntegerField()
    price = models.IntegerField()
    img = models.CharField(max_length=500, default='')
    catergories = models.CharField(max_length=1000, default='')

    def __str__(self):
        return '%s %s %s %s %s' % (self.name, self.availability, self.price, self.img,self.catergories )

    def release(stationery):
        b = {}
        b['name'] = stationery.get('name', '')
        b['availability'] = stationery.get('availability', '')
        b['price'] = stationery.get('price', '')
        b['img'] = stationery.get('img', '')
        b['catergories'] = stationery.get('catergories', '')
        return b
