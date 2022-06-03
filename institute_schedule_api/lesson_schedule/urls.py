from django.urls import path

from .views import *

urlpatterns = [
    path('lessons', LessonScheduleListView.as_view())
]