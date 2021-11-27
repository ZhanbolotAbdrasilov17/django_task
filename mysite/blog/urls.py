from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list),
    path('home', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('galary/', galary, name='galary'),


]