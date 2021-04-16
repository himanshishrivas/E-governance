from django.db import models

# Create your models here.

class gas_supply_demand(models.Model):
    user_name = models.CharField(max_length=30, default='Jane')
    info_type = models.CharField(max_length=30, default='symptoms')
    med_history = models.CharField(max_length=30, default='Fever')

class complain_manage(models.Model):
    med_history_id = models.IntegerField(default=0)
    med_history = models.CharField(max_length=100, default='symptoms')
    label = models.CharField(max_length=100, default='symptoms')
    type = models.CharField(max_length=100, default='symptoms')