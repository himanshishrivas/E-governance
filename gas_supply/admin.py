from django.contrib import admin
from .models import gas_supply_demand
from .models import complain_manage
# Register your models here.
admin.site.register(gas_supply_demand)
admin.site.register(complain_manage)