from django.urls import path
from . import views
from .views import PostDetailView, PostListView

urlpatterns = [
    path ('', views.home, name='reviewproduct-home'),
    path('about/', views.about, name='reviewProduct-about'),
    path('contact/', views.contact, name='reviewProduct-contact'),
    path('products/', views.products, name='reviewProduct-products'),
    path('IphoneX/', views.IphoneX, name='reviewProduct-IphoneX'),
    path('gtx3080/', views.gtx3080, name='reviewProduct-gtx3080'),
    path('ryzen9/', views.ryzen9, name='reviewProduct-ryzen9'),
    path('report/', PostListView.as_view(), name='reviewproduct-report'),
    path('review/<int:pk>', PostDetailView.as_view(), name='review-review_text'),
    path('review/new', PostCreateView.as_view(), name='review-create'),

]