# from statistics import mode
from typing import List
from django.db import models
from institute_infrastructure.models import *
from .constants import *

# Create your models here.


class Lesson(models.Model):
    class LessonNumber(models.IntegerChoices):
        FIRST   = 1, "1. " + FIRST_LESSON_NAME
        SECOND  = 2, "2. " + SECOND_LESSON_NAME
        THIRD   = 3, "3. " + THIRD_LESSON_NAME
        FOURTH  = 4, "4. " + FOURTH_LESSON_NAME
        FIFTH   = 5, "5. " + FIFTH_LESSON_NAME
        SIXTH   = 6, "6. " + SIXTH_LESSON_NAME
        SEVENTH = 7, "7. " + SEVENTH_LESSON_NAME 

    class LessonType(models.IntegerChoices):
        LABORATORY_WORK = 1, LABORATORY_WORK_NAME
        PRACTITE        = 2, PRACTICE_NAME
        LECTURE         = 3, LECTURE_NAME

    class WeekType(models.IntegerChoices):
        ODD     = 1, ODD_WEEK_NAME
        EVEN    = 2, EVEN_WEEK_NAME

    class WeekDay(models.IntegerChoices):
        MONDAY    = 1, MONDAY_NAME
        TUESDAY   = 2, TUESDAY_NAME
        WEDNESDAY = 3, WEDNESDAY_NAME
        THURSDAY  = 4, THURSDAY_NAME
        FRIDAY    = 5, FRIDAY_NAME
        SATURDAY  = 6, SATURDAY_NAME

    name = models.CharField(verbose_name="Нименование", max_length=100)

    number = models.IntegerField(verbose_name="Номер пары", choices=LessonNumber.choices)

    lesson_type = models.IntegerField(verbose_name="Тип пары", choices=LessonType.choices)
    
    week_type = models.IntegerField(verbose_name="Тип недели", choices=WeekType.choices)

    week_day = models.IntegerField(verbose_name="День недели", choices=WeekDay.choices)

    discipline = models.ForeignKey(Discipline, verbose_name="Дисциплина", on_delete=models.PROTECT)
    
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.PROTECT)

    begin = models.DateField(verbose_name="C",)

    end = models.DateField(verbose_name="По")

    group = models.ForeignKey(Group, verbose_name="Группа", related_name="lessons", on_delete=models.CASCADE)

    subgroup_number = models.IntegerField(verbose_name="Номер подгруппы (0 - для всех)", default=0, validators=[
            MinValueValidator(0, message="Значение не может быть меньше 0")
    ])

    building = models.ForeignKey(Building, verbose_name="Корпус", related_name="lessons", on_delete=models.PROTECT)

    classroom = models.ForeignKey(Classroom, verbose_name="Аудитория", related_name="lessons", on_delete=models.PROTECT)

    schedule = models.ForeignKey('LessonSchedule', verbose_name="Рапсиание", related_name="lessons", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name

    @property
    def with_groups(self) -> List[Group]:
        result = []

        lessons = Lesson.objects.filter(
            # end=self.end,
            classroom=self.classroom,
            discipline=self.discipline,
            teacher=self.teacher,
            number=self.number,
            week_day=self.week_day,
            week_type=self.week_type
        )
        for lesson in lessons:
            if lesson.group.id == self.group.id:
                continue
            result.append(lesson.group)
        return result

                
            
class LessonSchedule(models.Model):
    
    name = models.CharField(
        verbose_name="Наименование", 
        max_length=100
        )

    group = models.ForeignKey(
        Group, 
        verbose_name="Группа", 
        related_name='lesson_schedules', 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    @property
    def odd_week_lessons(self):
        return self.lessons.filter(week_type=Lesson.WeekType.ODD)

    @property
    def even_week_lessons(self):
        return self.lessons.filter(week_type=Lesson.WeekType.EVEN)


    @property
    def odd_week_monday_lessons(self):
        return self.lessons.filter(
            week_type=Lesson.WeekType.ODD,
            week_day=Lesson.WeekDay.MONDAY
        )


    @property
    def odd_week_tuesday_lessons(self):
        return self.lessons.filter(
            week_day=Lesson.WeekDay.TUESDAY,
            week_type=Lesson.WeekType.ODD
        )


    @property
    def odd_week_wednesday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.ODD,
            week_day=Lesson.WeekDay.WEDNESDAY
        )


    @property
    def odd_week_thursday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.ODD,
            week_day=Lesson.WeekDay.THURSDAY
        )

    @property
    def odd_week_friday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.ODD,
            week_day=Lesson.WeekDay.FRIDAY
        )

    @property
    def odd_week_saturday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.ODD,
            week_day=Lesson.WeekDay.SATURDAY
        )


    # EVEN WEEK

    @property
    def even_week_monday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.EVEN,
            week_day=Lesson.WeekDay.MONDAY
        )

    @property
    def even_week_tuesday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.EVEN,
            week_day=Lesson.WeekDay.TUESDAY
        )

    @property
    def even_week_wednesday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.EVEN,
            week_day=Lesson.WeekDay.WEDNESDAY
        )

    @property
    def even_week_thursday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.EVEN,
            week_day=Lesson.WeekDay.THURSDAY
        )

    @property
    def even_week_friday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.EVEN,
            week_day=Lesson.WeekDay.FRIDAY
        )

    @property
    def even_week_saturday_lessons(self) -> List[Lesson]:
        return self.lessons.filter(
            week_type=Lesson.WeekType.EVEN,
            week_day=Lesson.WeekDay.SATURDAY
        )
