# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class  Book(models.Model):
    name = models.CharField(max_length=100)
    availability = models.IntegerField()
    price = models.IntegerField()
    author = models.CharField(max_length=200, default='')
    img = models.CharField(max_length=500, default='')
    catergories = models.CharField(max_length=1000, default='')

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.name, self.availability, self.price, self.img, self.author,self.catergories )

    def release(book):
        b = {}
        b['name'] = book.get('name', '')
        b['availability'] = book.get('availability', '')
        b['price'] = book.get('price', '')
        b['author'] = book.get('author', '')
        b['img'] = book.get('img', '')
        b['catergories'] = book.get('catergories', '')
        return b
