"""institute_schedule_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from institute_infrastructure.views import group_views, teacher_views, chair_views, building_views, classroom_views, discipline_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/groups', group_views.GroupList.as_view()),
    path('api/groups/<int:id>', group_views.GroupDetail.as_view()),
    path('api/teachers', teacher_views.TeacherList.as_view()),
    path('api/teachers/<int:id>', teacher_views.TeacherDetail.as_view()),
    path('api/chairs', chair_views.ChairList.as_view()),
    path('api/chairs/<int:id>', chair_views.ChairDetail.as_view()),
    path('api/buildings', building_views.BuildingList.as_view()),
    path('api/buildings/<int:id>', building_views.BuildingDetails.as_view()),
    path('api/classrooms', classroom_views.ClassroomList.as_view()),
    path('api/classrooms/<int:id>', classroom_views.ClassroomDetails.as_view()),
    path('api/disciplines', discipline_views.DisciplineList.as_view()),
    path('api/disciplines/<int:id>', discipline_views.DisciplineDetails.as_view())
]
