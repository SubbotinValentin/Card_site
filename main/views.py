from django.shortcuts import render, get_object_or_404 

from .models import Works, Category

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Проекты', 'url_name': 'projects'},
        {'title': 'Задачи', 'url_name': 'tasks'}
]


def index(request):
    context = {
        'page': 'Главная',
        'menu': menu,
    }
    return render(request, 'main/index.html', context=context)


def projects(request):
    posts = Works.objects.filter(cat_id=1)
    context = {
        'page': 'Проекты',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'main/projects.html', context=context)


def tasks(request):
    posts = Works.objects.filter(cat_id=2)
    context = {
        'page': 'Задачи',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'main/tasks.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Works, slug=post_slug)
    context = {
        'page': 'Задачи',
        'menu': menu,
        'post': post,
        'cat_select': post.cat_id,
    } 
    return render(request, 'main/post.html', context=context)