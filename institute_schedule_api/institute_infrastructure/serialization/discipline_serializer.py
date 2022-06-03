from rest_framework import serializers

class DisciplineSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(read_only=True)