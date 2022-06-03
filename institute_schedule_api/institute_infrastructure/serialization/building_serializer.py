from rest_framework import serializers

class PropertyClassroomSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    name = serializers.CharField()


class BuildingPreViewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)

    name = serializers.CharField(read_only=True)

    shortName = serializers.CharField(read_only=True)


class BuildingSerializer(BuildingPreViewSerializer):
    classrooms = PropertyClassroomSerializer(many=True)