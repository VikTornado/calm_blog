from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm
from django.contrib import messages  # 🔥 додати

def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'news/news_detail.html', {'news': news_item})

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, "Новину успішно створено ✅")
            return redirect('news_detail', slug=news.slug)
    else:
        form = NewsForm()
    return render(request, 'news/news_create.html', {'form': form})