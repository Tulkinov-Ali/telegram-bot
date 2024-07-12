from django.contrib import admin
from bot.models import Products, Tg_user, Category


class ProductsList(admin.ModelAdmin):
    list_display = ['name', 'ctg', 'img', 'price', 'desc']


class Tg_userList(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'surname', 'username', 'phone', 'lang', 'log']


class CategoryList(admin.ModelAdmin):
    list_display = ['name', 'img']

admin.site.register(Tg_user, Tg_userList)
admin.site.register(Products, ProductsList)
admin.site.register(Category, CategoryList)
