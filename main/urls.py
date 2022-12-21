from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('projects/', projects, name='projects'),
    path('tasks/', tasks, name='tasks'),
    path('post/<slug:post_slug>/', show_post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)