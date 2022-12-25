from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *


class IndexHome(DataMixin, ListView):
    model = Category
    template_name = 'main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['page'] = 'Главная'
        return dict(list(context.items()) + list(c_def.items()))


class AboutHome(DataMixin, ListView):
    model = Category
    template_name = 'main/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['page'] = 'Главная'
        return dict(list(context.items()) + list(c_def.items()))


# def index(request):
#     context = {
#         'page': 'Главная',
#         'menu': menu,
#     }
#     return render(request, 'main/index.html', context=context)


class ProjectsHome(DataMixin, ListView):
    model = Works
    template_name = 'main/projects.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['page'] = 'Проекты'
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Works.objects.all()


# def projects(request):
#    posts = Works.objects.filter(cat_id=1)
#    context = {
#        'page': 'Проекты',
#        'menu': menu,
#        'posts': posts,
#    }
#     return render(request, 'main/projects.html', context=context)


class ShowPost(DataMixin, DetailView):
    model = Works
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'    #(pk_url_kwarg - для ключа(id))
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['page'] = context['post']
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(Works, slug=post_slug)
#     context = {
#         'page': 'Задачи',
#         'menu': menu,
#         'post': post,
#         'cat_select': post.cat_id,
#     }
#     return render(request, 'main/post.html', context=context)


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['page'] = 'Добавить'
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(request, 'main/addpage.html', {'page': 'Добавить', 'menu': menu, 'form': form})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        context['page'] = 'Регистрация'
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')