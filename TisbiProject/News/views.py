from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


# Create your views here.
def main_page(request):
    news = News.objects.filter(is_published=True).order_by('-pk')
    print(news)
    return render(request, 'News/news_page.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_main_page')
        else:
            error = 'форма была заполенан не верно'
    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'News/create.html', data)
