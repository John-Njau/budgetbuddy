from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.FloatField()
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return self.description