from django.contrib import admin

from institute_infrastructure.models import *

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('Преподаватель','chair')
    
    @admin.display()
    def Преподаватель(self, obj):
        return obj

    @admin.display(ordering='Кафедра')
    def Кафедра(self, obj):
        return obj

# Register your models here.
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Group)
admin.site.register(Building)
admin.site.register(Discipline)
admin.site.register(Classroom)
admin.site.register(Chair)
