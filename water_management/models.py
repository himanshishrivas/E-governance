from django.db import models

# Create your models here.
class resource_manage(models.Model):
    #insid = models.IntegerField(default=0)
    user_name = models.CharField(max_length=20, default='Himanshi')
    first_name = models.CharField(max_length=20, default=' ')
    last_name = models.CharField(max_length=20, default='Shrivas')
    #initial = models.CharField(max_length=20, default='x')
    #relationToPatient = models.CharField(max_length=20, default='parent to children')
    dob = models.CharField(max_length=30, default='now')
    #socSec = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default='main st')
    city = models.CharField(max_length=20, default='columbus')
    state = models.CharField(max_length=20, default='OH')
    zip = models.CharField(max_length=20, default='43201')
    adhaar_Number = models.CharField(max_length=20, default='6144445566')
    cellphone = models.CharField(max_length=20, default='6144445566')
    email = models.CharField(max_length=20, default='example@emamil.com')
    '''
     employerName = models.CharField(max_length=20, default='John')
    employerOccupation = models.CharField(max_length=20, default='manager')
    employerBusAddr = models.CharField(max_length=20, default='main st')
    employerBusPhone = models.CharField(max_length=20, default='6144445566')
    employerBusEmail = models.CharField(max_length=20, default='example@email.com')
    insurComp = models.CharField(max_length=20, default='franklin')
    insurCompPhone = models.CharField(max_length=20, default='6144445566')
    insurContNum = models.CharField(max_length=20, default='6144445566')
    insurGroupNum = models.CharField(max_length=20, default='6144445566')
    insurSubscNum = models.CharField(max_length=20, default='6144445566')
    dependentName = models.CharField(max_length=20, default='Jane Doe')

'''

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
