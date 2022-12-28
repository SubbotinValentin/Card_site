from django.contrib import admin

from .models import *

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create', 'cat')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'cat')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('time_create', 'cat')
    prepopulated_fields = {'slug': ('title',)}