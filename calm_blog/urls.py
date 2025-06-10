from django.contrib import admin
from django.urls import path, include  # 🔥 додаємо include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from news import views as news_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_views.news_list, name='news_list'),
    path('news/<slug:slug>/', news_views.news_detail, name='news_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='news_list'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ тепер працює
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
