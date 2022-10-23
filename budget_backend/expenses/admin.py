from django.contrib import admin

from .models import Expense, Category, Author, Article

# Register your models here.
admin.site.register(Expense)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Article)
