from django.contrib import admin

# Register your models here.
from .models import Category, CategoryDetails


admin.site.register(Category)
admin.site.register(CategoryDetails)
