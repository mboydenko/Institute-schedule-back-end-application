from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Discipline(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

class Chair(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    abbreviation = models.CharField(max_length=20, verbose_name="Аббревиатура")

    def __str__(self) -> str:
        return self.abbreviation

class Teacher(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    email = models.CharField(max_length=100, verbose_name="Эл. почта")
    chair = models.ForeignKey(Chair, verbose_name="Кафедра", related_name="teachers", on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name[0]}"
    
    @property
    def subject(self):
        return self

class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    
    number_of_subgroups = models.IntegerField(
        verbose_name = "Количество подгрупп", 
        default = 0,
        validators=[
            MinValueValidator(0, message="Значение не может быть меньше 0")
        ]
    )

    def has_subgroups(self) -> bool:
        if self.number_of_subgroups > 1:
            return True
        return False

    def __str__(self) -> str:
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    short_name = models.CharField(max_length=20, verbose_name="Короткое имя")

    def __str__(self) -> str:
        return self.short_name

class Classroom(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    building = models.ForeignKey(Building, verbose_name="Корпус", related_name='classrooms', on_delete=models.PROTECT)
    
    class Meta:
        verbose_name="Аудитория"
        verbose_name_plural="Аудитории"

    def __str__(self):
        return f"{self.building.name} {self.name}"

    @property
    def get_name(self):
        return self
