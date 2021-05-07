from django.urls import path
from . import views
from .views import PostDetailView, PostListView3080, PostListViewiphoneX, PostListViewryzen , PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls import url


urlpatterns = [
    path ('', views.home, name='reviewproduct-home'),
    path('about/', views.about, name='reviewProduct-about'),
    path('contact/', views.contact, name='reviewProduct-contact'),
    path('products/', views.products, name='reviewProduct-products'),
    path('IphoneX/', PostListViewiphoneX.as_view(), name='reviewProduct-IphoneX'),
    path('gtx3080/', PostListView3080.as_view(), name='reviewProduct-gtx3080'),
    path('ryzen9/', PostListViewryzen.as_view(), name='reviewProduct-ryzen9'),
    path('review/<int:pk>', PostDetailView.as_view(), name='review-review_text'),
    path('review/new', PostCreateView.as_view(), name='review-create'),
    path('review/<int:pk>/update/', PostUpdateView.as_view(), name='review-update'),
    path('review/<int:pk>/delete/', PostDeleteView.as_view(), name='review-delete'),
    path('review/password', views.change_password, name='change_password'),]