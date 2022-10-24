from django.contrib import admin
from savings.models import Saving, SavingTarget

# Register your models here.
admin.site.register(Saving)
admin.site.register(SavingTarget)