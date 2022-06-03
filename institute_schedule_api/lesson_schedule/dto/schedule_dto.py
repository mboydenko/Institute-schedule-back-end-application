from typing import List

class DateDto:
    year: int = 0
    month: int = 0
    day: int = 0


class LessonDto:
    discipline_id: int
    lesson_type: int
    lesson_number: int
    teacher_id: int
    subgroup_number: int
    building_id: int
    classroom_id: int
    begin: DateDto
    end: DateDto


class ScheduleDto:
    mondayLessons: List[LessonDto]    = []
    tuesdayLessons: List[LessonDto]   = []
    wednesdayLessons: List[LessonDto] = []
    thursdayLessons: List[LessonDto]  = []
    fridayLessons: List[LessonDto]    = []
    saturdayLessons: List[LessonDto]  = []
    