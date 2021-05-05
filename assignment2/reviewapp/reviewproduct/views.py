from django.shortcuts import render

def home(request):
    return render(request, 'reviewproduct/home.html', {'title': 'Home'})
def about (request):
    return render(request, 'reviewproduct/about.html', {'title': 'About Us'})
def contact (request):
        return render(request, 'reviewproduct/contact.html', {'title': 'Contact'})
def products (request):
        return render(request, 'reviewproduct/products.html', {'title': 'Products'})
def IphoneX (request):
        return render(request, 'reviewproduct/IphoneX.html', {'title': 'IphoneX'})
def ryzen9 (request):
        return render(request, 'reviewproduct/ryzen9.html', {'title': 'ryzen9 3800x'})
def gtx3080 (request):
        return render(request, 'reviewproduct/gtx3080.html', {'title': 'gtx3080'})


