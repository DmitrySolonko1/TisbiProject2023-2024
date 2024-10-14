from django.urls import path, include
from .views import main_page, create

urlpatterns = [
    path('', main_page, name='news_main_page'),
    path('create/', create, name='news_create_page'),
]
