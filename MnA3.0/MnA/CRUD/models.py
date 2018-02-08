from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Audit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='%(class)ss_creators',
        on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='%(class)ss_updators',
        on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Deal(Audit):
    deal_number = models.CharField(verbose_name="Deal Number", max_length=200, primary_key=True)
    ann_date = models.DateField('Announced Date')
    effective_date = models.DateField('Effective Date', null=True, blank=True)
    cancel_date = models.DateField('Cancel Date', null=True, blank=True)
    total_value = models.DecimalField("Total Deal Value", decimal_places=2, max_digits=13)

    acq_companyName = models.CharField(verbose_name="Acq Company Name", max_length=200)
    acq_country = models.CharField(verbose_name="Acq Country Code", max_length=3)
    acq_sector = models.CharField(verbose_name="Acq Sector", max_length=200)

    tar_companyName = models.CharField(verbose_name="Tar Company Name", max_length=200)
    tar_country = models.CharField(verbose_name="Tar Country Code", max_length=3)
    tar_sector = models.CharField(verbose_name="Tar Sector", max_length=200)

#Todo make country and sector choice fields


class DealHistory(Audit):
    poke_id = models.AutoField(primary_key=True)
    date_poked = models.DateTimeField(verbose_name="Datetime Poked")
    deal = models.ForeignKey(Deal, verbose_name="Deal", on_delete=models.SET_NULL, null=True, blank=True)

#class Pokes(models.Model):
#   deal = models.ForeignKey(Deal, )
#  deal_history = models.ForeignKey(DealHistory, )
#    field_change = models.CharField(verbose_name="Field Changed", max_length=200)
#    old_value = models.CharField(verbose_name="Old Value", max_length=200)
#   new_value = models.CharField(verbose_name="New Value", max_length=200)
