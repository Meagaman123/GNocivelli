from django.shortcuts import render, redirect
from .models import Review
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Review

        success_url= '/products'
        def test_func(self):
                review = self.get_object()
                if self.request.user == review.author:
                        return True
                return False
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        def test_func(self):
                review = self.get_object()
                if self.request.user == review.author:
                        return True
                return False
        model = Review
        fields = ['product_rating', 'review_text', 'Date_review']

class PostListViewryzen(ListView):
        paginate_by = 5
        model = Review
        template_name = 'reviewproduct/ryzen9.html'
        context_object_name = 'reviews'
        ordering = ['-Date_review']

class PostListView3080(ListView):
        paginate_by = 5
        model = Review
        template_name = 'reviewproduct/gtx3080.html'
        context_object_name = 'reviews'
        ordering = ['-Date_review']

class PostListViewiphoneX(ListView):
        paginate_by = 5
        model = Review
        template_name = 'reviewproduct/IphoneX.html'
        context_object_name = 'reviews'
        ordering = ['-Date_review']

class PostDetailView(DetailView):
        model = Review

class PostCreateView(LoginRequiredMixin, CreateView):
        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)
        model = Review
        fields = ['product', 'product_rating', 'review_text', 'Date_review']


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

def change_password(request):
        if request.method == 'POST':
                form = PasswordChangeForm(request.user, request.POST)
                if form.is_valid():
                        user = form.save()
                        update_session_auth_hash(request, user)
                        messages.success(request, 'Your password was successfully updated!')
                        return redirect('/profile/')
                else:
                        messages.error(request, 'please correct the error below.')
        else:
                form = PasswordChangeForm(request.user)
        return render(request, 'reviewproduct/changepassword.html' , {'form': form})                
