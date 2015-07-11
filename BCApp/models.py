from django.db import models

# Create your models here.


class BCBusinessUnit(models.Model):
    name = models.CharField(max_length=250)
    outcomeOneTime = models.FloatField()
    outcomeMonthly = models.FloatField()
    incomeMonthly = models.FloatField()
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class BCBusinessModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=2050)
    businessunits = models.ManyToManyField(BCBusinessUnit)

    def __str__(self):
        return self.name

class BCUser(models.Model):
    username = models.CharField(max_length=250)
    businessmodels = models.ManyToManyField(BCBusinessModel)
    businessunits = models.ManyToManyField(BCBusinessUnit)

    def __str__(self):
        return self.username

