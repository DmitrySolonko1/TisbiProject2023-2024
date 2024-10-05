from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('about/', views.about, name='about_page')
]
