from django.db import models
from institute_infrastructure.models import *

# Create your models here.
class Courswork(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=100)

    discipline = models.ForeignKey(Discipline, verbose_name="Дисциплина", on_delete=models.CASCADE)

    date = models.DateField(verbose_name="Дата")

    time = models.TimeField(verbose_name="Время")

    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)

    teachers = models.ManyToManyField(Teacher, verbose_name="Состав коммисии", related_name="courseworks")

    building = models.ForeignKey(Building, verbose_name="Корпус", related_name="courseworks", on_delete=models.CASCADE)

    classroom = models.ForeignKey(Classroom, verbose_name="Аудитория", related_name="courseworks", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
