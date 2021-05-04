from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Review Product - Home</h1>')
def about (request):
    return HttpResponse('<h1> Review Product - About Us</h1>')
def contact (request):
        return HttpResponse('<h1> Review Product - About Us</h1>')
def products (request):
        return HttpResponse('<h1> Review Product - About Us</h1>')