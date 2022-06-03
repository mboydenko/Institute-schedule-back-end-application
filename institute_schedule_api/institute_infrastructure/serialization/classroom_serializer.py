from rest_framework import serializers


class BuildingPropertySerializer(serializers.Serializer):
    id = serializers.IntegerField()

    name = serializers.CharField(read_only=True)

    short_name = serializers.CharField(read_only=True)


class ClassroomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.IntegerField(read_only=True)

    building = BuildingPropertySerializer(read_only=True)

