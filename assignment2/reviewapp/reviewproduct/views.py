from django.shortcuts import render

def home(request):
    return render(request, 'reviewproduct/home.html')
def about (request):
    return render(request, 'reviewproduct/about.html')
def contact (request):
        return render(request, 'reviewproduct/contact.html')
def products (request):
        return render(request, 'reviewproduct/products.html')