from django.db import models


# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Income(models.Model):
    amount = models.FloatField()
    notes = models.CharField(max_length=255)
    # source = models.ForeignKey(Source,on_delete=models.CASCADE)
    source_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.source_name

# Path: budget_backend\income\serializers.py
# Compare this snippet from budget_backend\budget\serializers.py:
