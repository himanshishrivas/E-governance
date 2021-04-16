from django.contrib import admin
from .models import resource_manage, complain_manage
# Register your models here.
admin.site.register(resource_manage)
admin.site.register(complain_manage)