from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexHome.as_view(), name='home'),
    path('projects/', ProjectsHome.as_view(), name='projects'),
    path('tasks/', TasksHome.as_view(), name='tasks'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('addpage/', AddPage.as_view(), name='addpage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)