from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import News
from .forms import NewsForm


# Create your views here.
def main_page(request):
    news = News.objects.filter(is_published=True).order_by('-pk')
    print(news)
    return render(request, 'News/news_page.html', {'news': news})


# class MainPageNews(ListView):
#     model = News
#     template_name = 'News/news_page.html'
#     context_object_name = 'news'
#
#     def get_queryset(self):
#         return News.objects.filter(is_published=True).order_by('-pk')


class NewsDetailPage(DetailView):
    model = News
    template_name = 'News/news_detail_page.html'
    context_object_name = 'article'


class NewsUpdatePage(UpdateView):
    model = News
    template_name = 'News/create.html'
    form_class = NewsForm


class NewsDeletePage(DeleteView):
    model = News
    template_name = 'News/news_delete_page.html'
    success_url = '/news'


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
