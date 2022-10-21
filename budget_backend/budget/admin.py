from django.contrib import admin
from budget.models import Category, Expense

# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)