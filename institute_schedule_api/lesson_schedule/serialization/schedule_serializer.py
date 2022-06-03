from rest_framework import serializers

from .lesson_serializer import LessonSerializer


class GroupPropertySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(read_only=True)


class ScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(read_only=True)

    group = GroupPropertySerializer(read_only=True)

    odd_week_monday_lessons = LessonSerializer(many=True, read_only=True)

    odd_week_tuesday_lessons = LessonSerializer(many=True, read_only=True)

    odd_week_wednesday_lessons = LessonSerializer(many=True, read_only=True)

    odd_week_thursday_lessons = LessonSerializer(many=True, read_only=True)

    odd_week_friday_lessons = LessonSerializer(many=True, read_only=True)

    odd_week_saturday_lessons = LessonSerializer(many=True, read_only=True)

    even_week_monday_lessons = LessonSerializer(many=True, read_only=True)

    even_week_tuesday_lessons = LessonSerializer(many=True, read_only=True)

    even_week_wednesday_lessons = LessonSerializer(many=True, read_only=True)

    even_week_thursday_lessons = LessonSerializer(many=True, read_only=True)

    even_week_friday_lessons = LessonSerializer(many=True, read_only=True)

    even_week_saturday_lessons = LessonSerializer(many=True, read_only=True)