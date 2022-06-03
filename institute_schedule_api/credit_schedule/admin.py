from django.contrib import admin
from .models import *

# Register your models here.

class CreditAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'group',
        'subgroup_number',
        'teacher',
        'discipline',
        'classroom',
        'date',
        'time',
        
    )
    

admin.site.register(Credit, CreditAdmin)