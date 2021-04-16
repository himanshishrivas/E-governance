from django.db import models
#from _datetime import timezone

# Create your models here.
class electricity_supply(models.Model):
    user_name = models.CharField(max_length=20, default='larryxu')
    meds_name = models.CharField(max_length=50, default='Oxi')
    meds_strength = models.CharField(max_length=30, default='40 mg p.o.')
    meds_dir = models.CharField(max_length=20, default='daily')
    meds_status = models.CharField(max_length=20, default='active')
    meds_date = models.CharField(max_length=20, default='now')

class complain_manage(models.Model):
    user_name = models.CharField(max_length=30, default="xxx")
    first_name = models.CharField(max_length=20, default='Himanshi')
    middle_name = models.CharField(max_length=20, default=' ')
    last_name = models.CharField(max_length=20, default='Shrivas')
    address = models.CharField(max_length=30, default='Alok nagar')
    city = models.CharField(max_length=20, default='Indore')
    state = models.CharField(max_length=2, default='M.P')
    zipCode = models.CharField(max_length=12, default='452017')
    adhaar_Number = models.CharField(max_length=12, default='614455567817')
    cellPhone = models.CharField(max_length=10, default='6144567890')
    email = models.CharField(max_length=30, default='himanshi@gmail.com')
