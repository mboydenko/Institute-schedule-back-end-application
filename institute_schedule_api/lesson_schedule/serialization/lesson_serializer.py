from rest_framework import serializers

from institute_infrastructure.serialization import teacher_serializer
from institute_infrastructure.serialization import group_serializer
from institute_infrastructure.serialization import discipline_serializer

class PropertyBuidingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(read_only=True)

    short_name = serializers.CharField(read_only=True)

class PropertyClassroomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

class LessonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    
    name = serializers.CharField(read_only=True)

    number = serializers.IntegerField(read_only=True)

    lesson_type = serializers.IntegerField(read_only=True)

    week_type = serializers.IntegerField(read_only=True)

    week_day = serializers.IntegerField(read_only=True)

    teacher = teacher_serializer.TeacherPreViewSerializer()

    discipline = discipline_serializer.DisciplineSerializer(read_only=True)

    group = group_serializer.GroupSerializer(read_only=True)

    with_groups = group_serializer.GroupSerializer(many=True, read_only=True)

    begin = serializers.DateField(read_only=True)

    end = serializers.DateField(read_only=True)

    subgroup_number = serializers.IntegerField(read_only=True)

    building = PropertyBuidingSerializer(read_only=True)

    classroom = PropertyClassroomSerializer(read_only=True)

