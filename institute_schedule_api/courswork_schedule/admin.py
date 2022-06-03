from django.contrib import admin
from .models import *

# Register your models here.
class CourseworkAdmin(admin.ModelAdmin):
    filter_horizontal = ["teachers",]
 
admin.site.register(Courswork, CourseworkAdmin)