from django.shortcuts import render
from .models import Category, News


# Create your views here.
def main_page(request):
    news = News.objects.all()
    print('news: ', news)
    return render(request, 'News/news_page.html', {'news': news})
