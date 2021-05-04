from django.shortcuts import render

def home(request):
    return render(request, 'reviewproduct/home.html', {'title': 'Home'})
def about (request):
    return render(request, 'reviewproduct/about.html', {'title': 'About Us'})
def contact (request):
        return render(request, 'reviewproduct/contact.html', {'title': 'Contact'})
def products (request):
        products={
            'products': products.objects.all()
        }
        return render(request, 'reviewproduct/products.html', {'title': 'Procucts'})


