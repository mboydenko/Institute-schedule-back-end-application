from django.db import models

from institute_infrastructure.models import Group, Teacher, Discipline, Building, Classroom

# Create your models here.
class Exam(models.Model):
    class ExamType(models.enums.IntegerChoices):
        EXAM = 1, "Экзамент"
        CONSULTATION = 2, "Консультация"

    name = models.CharField(max_length=100, verbose_name="Наименование")

    exam_type = models.IntegerField(verbose_name="Тип", choices=ExamType.choices)

    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE)

    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE)

    discipline = models.ForeignKey(Discipline, verbose_name="Дисциплина", on_delete=models.CASCADE)

    building = models.ForeignKey(Building, verbose_name="Корпус", on_delete=models.CASCADE)

    classroom = models.ForeignKey(Classroom, verbose_name="Аудитория", on_delete=models.CASCADE)

    date = models.DateField(verbose_name="Дата")

    time = models.TimeField(verbose_name="Время")

    def __str__(self):
        return self.name
 