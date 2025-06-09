from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image', 'author']
        widgets = {
            'slug': forms.TextInput(attrs={'readonly': 'readonly'}),
        }