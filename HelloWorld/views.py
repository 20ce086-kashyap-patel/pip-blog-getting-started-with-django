from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # response = HttpResponse('Hello, World!')
    response = render(request, 'index.html')
    return response