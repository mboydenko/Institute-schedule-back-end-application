from django.contrib import admin
from .models import *

# Register your models here.

class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'teacher', 'discipline' , 'exam_type', 'date', 'time')

admin.site.register(Exam, ExamAdmin)