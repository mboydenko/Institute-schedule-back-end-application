from django.db import models
from django.core.validators import MinValueValidator

from institute_infrastructure.models import Group, Teacher, Discipline, Building, Classroom

# Create your models here.
class Credit(models.Model):

    name = models.CharField(max_length=100, verbose_name="Наименование")

    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)

    subgroup_number = models.IntegerField(verbose_name="Номер подгруппы (0 - для всех)", default=0, validators=[
            MinValueValidator(0, message="Значение не может быть меньше 0")
    ])

    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE)

    discipline = models.ForeignKey(Discipline, verbose_name="Дисциплина", on_delete=models.CASCADE)

    building = models.ForeignKey(Building, verbose_name="Корпус", on_delete=models.CASCADE)

    classroom = models.ForeignKey(Classroom, verbose_name="Аудитория", on_delete=models.CASCADE)

    date = models.DateField(verbose_name="Дата")

    time = models.TimeField(verbose_name="Время")
 