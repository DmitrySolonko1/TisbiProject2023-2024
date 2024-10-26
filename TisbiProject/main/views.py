from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title": "Main index page1231231231232",
        "values": ["hello", "wOrLd", "123"]
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
