

from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news_item})
