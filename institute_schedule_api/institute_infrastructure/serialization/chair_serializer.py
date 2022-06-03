from rest_framework import serializers

class PropertyTeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    first_name = serializers.CharField(read_only=True)

    last_name = serializers.CharField(read_only=True)

    middle_name = serializers.CharField(read_only=True)

    email = serializers.CharField(read_only=True)


class ChairPreViewSerializor(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(read_only=True)

    abbreviation = serializers.CharField(read_only=True)


class ChairSerializer(ChairPreViewSerializor):
    teachers = PropertyTeacherSerializer(many=True)