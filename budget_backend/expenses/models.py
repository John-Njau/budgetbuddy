from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    notes = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.category.name

    # TODO add user field
    def __str__(self):
        return self.title
