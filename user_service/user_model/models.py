from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

class user_registration(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):

        return '%s %s %s %s %s %s' % (self.fname, self.lname, self.
                                      email, self.mobile, self.password, self.address)
