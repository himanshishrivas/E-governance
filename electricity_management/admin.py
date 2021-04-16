from django.contrib import admin
from .models import electricity_supply, complain_manage

# Register your models here.
admin.site.register(electricity_supply)
admin.site.register(complain_manage)