from django.shortcuts import render
from .models import Review

def home(request):
    return render(request, 'reviewproduct/home.html', {'title': 'Home'})
def about (request):
    return render(request, 'reviewproduct/about.html', {'title': 'About Us'})
def contact (request):
        return render(request, 'reviewproduct/contact.html', {'title': 'Contact'})
def products (request):
        return render(request, 'reviewproduct/products.html', {'title': 'Products'})
def IphoneX (request):
        all_reviews = {
            'reviews': Review.objects.all()
        }
        return render(request, 'reviewproduct/IphoneX.html', all_reviews)
def ryzen9 (request):
        all_reviews = {
            'reviews': Review.objects.all()
        } 
        return render(request, 'reviewproduct/ryzen9.html', all_reviews)

def gtx3080 (request):
        all_reviews = {
            'reviews': Review.objects.all()
        }
 
        return render(request, 'reviewproduct/gtx3080.html',  all_reviews)


