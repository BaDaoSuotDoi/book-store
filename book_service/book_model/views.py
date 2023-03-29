from __future__ import unicode_literals
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from book_model.models.book import Book
from django.forms.models import model_to_dict

@csrf_exempt
def get_list_book(request):
    resp = {}
    books = Book.objects.all()
    temp = []
    for book in books.values() :
        print(book)
        temp.append(Book.release(book))

    print(temp)
    resp['books'] = temp
    return HttpResponse(json.dumps(resp), content_type='application/json')
