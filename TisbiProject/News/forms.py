from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Контет'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
        }
