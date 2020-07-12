from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    email = models.EmailField(null=True)
    contract_number = models.CharField(max_length=50)
    is_active = models.BooleanField()


class Meter(models.Model):
    contract = models.ForeignKey('Contract', models.SET_NULL, null=True)
    meter_number = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()


class DrainageArea(models.Model):
    contract = models.ForeignKey('Contract', models.SET_NULL, null=True)
    size = models.FloatField()


class ContractHistory(models.Model):
    contract = models.ForeignKey('Contract', models.CASCADE)
    meter = models.ForeignKey('Meter', models.CASCADE)
    begin = models.DateField(null=True)
    end = models.DateField(null=True)
