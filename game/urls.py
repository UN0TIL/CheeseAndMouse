from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='game/test.html'), name='test'),
    # path('', TemplateView.as_view(template_name='game/load_screen.html'), name='load_screen'),
    path('tap/', views.main_page_view, name='tap'),
    path('save_user_data/', views.save_user_data, name='save_user_data'),
    path('increment/', views.increment_count, name='increment'),
    path('multiplier/', views.upper, name='upper'),
    path('autoclick/', views.autoclick, name='autoclick'),
    path('friends/', views.friends_view, name='friends'),
    path('mission/', views.mission_view, name='mission'),
    path('tasks/', views.tasks_view, name='task'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)