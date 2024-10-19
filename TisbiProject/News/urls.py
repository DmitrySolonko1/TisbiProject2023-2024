from django.urls import path, include
from .views import main_page, create, NewsDetailPage, NewsUpdatePage, NewsDeletePage

urlpatterns = [
    path('', main_page, name='news_main_page'),
    path('create/', create, name='news_create_page'),
    path('<int:pk>', NewsDetailPage.as_view(), name='news_detail_page'),
    path('<int:pk>/update', NewsUpdatePage.as_view(), name='news_update_page'),
    path('<int:pk>/delete', NewsDeletePage.as_view(), name='news_delete_page'),
]
