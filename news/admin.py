from django.contrib import admin
from .models import News
from .forms import NewsForm

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('title', 'slug', 'author', 'created_at')
    readonly_fields = ('slug',)