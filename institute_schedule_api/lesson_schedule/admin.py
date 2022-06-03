from django.contrib import admin

from .models import *

class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'teacher', 'discipline', 'week_type', 'week_day', 'building', 'classroom', 'begin', 'end')
    # list_editable = ('group', 'teacher', 'discipline', 'week_day', 'building', 'classroom')

    # @property
    # def classroom(self):
    #     return self.classroom.name

# Register your models here.
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonSchedule)