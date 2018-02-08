from django.db import models

# Create your models here.
class Deal(models.Model):
    deal_number = models.CharField(verbose_name="Deal Number", max_length=200)
    ann_date = models.DateTimeField('Announced Date')
    effective_date = models.DateTimeField('Effective Date', null=True, blank=True)
    cancel_date = models.DateTimeField('Cancel Date', null=True, blank=True)
    total_value = models.DecimalField("Total Deal Value", decimal_places=2, max_digits=13)

    acq_companyName = models.CharField(verbose_name="Acq Company Name", max_length=200)
    acq_country = models.CharField(verbose_name="Acq Country Code", max_length=3)
    acq_sector = models.CharField(verbose_name="Acq Sector", max_length=200)

    tar_companyName = models.CharField(verbose_name="Tar Company Name", max_length=200)
    tar_country = models.CharField(verbose_name="Tar Country Code", max_length=3)
    tar_sector = models.CharField(verbose_name="Tar Sector", max_length=200)

#Todo make country and sector choice fields


class Poke(models.Model):
    value = models.CharField(verbose_name="Value to Poke In", max_length=200)
    field = models.CharField(verbose_name="Field to Poke", max_length=200)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)