from django.db import models

# Create your models here.


class SavingTarget(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    notes = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Saving Target"
        verbose_name_plural = "Saving Targets"


class Saving(models.Model):
    amount = models.FloatField()
    notes = models.CharField(max_length=255)
    target_amount = models.ForeignKey(SavingTarget, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return self.target_amount.name
