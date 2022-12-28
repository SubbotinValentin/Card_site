from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexHome.as_view(), name='home'),
    path('about', AboutHome.as_view(), name='about'),
    path('projects/', ProjectsHome.as_view(), name='projects'),
    path('post_projects/<slug:post_slug>/', ShowPost_projects.as_view(), name='post_projects'),
    path('post_skill/<slug:post_slug>/', ShowPost_skill.as_view(), name='post_skill'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('addpage/', AddPage.as_view(), name='addpage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)