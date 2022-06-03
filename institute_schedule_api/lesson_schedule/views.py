from rest_framework.views import APIView, Response
from .models import *
from .serialization.lesson_serializer import LessonSerializer
from .serialization.schedule_serializer import ScheduleSerializer

# Create your views here.
class LessonListView(APIView):
    def get(self, request):
        lessons = Lesson.objects.all()
        result = LessonSerializer(lessons, many=True)
        return Response(result.data)

class LessonScheduleListView(APIView):
    def get(self, request):
        schedules = LessonSchedule.objects.all()
        result = ScheduleSerializer(schedules, many=True)
        return Response(result.data)