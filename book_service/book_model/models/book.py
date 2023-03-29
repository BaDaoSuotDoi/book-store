# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class  Book(models.Model):
    name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s %s' % (self.name, self.availability, self.price)

    def release(book):
        b = {}
        b['name'] = book.get('name', '')
        b['availability'] = book.get('availability', '')
        b['price'] = book.get('price', '')
        return b
