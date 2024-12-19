from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.main_page_view, name='tap'),
    path('increment/', views.increment_count, name='increment'),
    path('multiplier/', views.upper, name='upper'),
    path('autoclick/', views.autoclick, name='autoclick'),
    path('test/', TemplateView.as_view(template_name='test/index_old.html'), name='test'),
    path('tasks/', views.tasks_view, name='task'),
    path('friends/', views.friends_view, name='friends'),
    path('mission/', views.mission_view, name='mission'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)