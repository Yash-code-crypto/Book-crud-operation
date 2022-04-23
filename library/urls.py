from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls import url
from . import views

app_name = 'library'
urlpatterns = [
  
    path('home', HomeView.as_view(), name='home'),
    path('user-signup', views.signup_user, name="user-signup"),
    path('', views.signin, name="signin"),



    path('logout/', LogoutView.as_view(next_page='library:signin'), name='logout'),

    path('books/', BookView.as_view(), name='book-list'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<slug:pk>/', BookDetail.as_view(), name= 'book'),
    path('book/<slug:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<slug:pk>/delete/', BookDelete.as_view(), name='book-delete'),



 

]
