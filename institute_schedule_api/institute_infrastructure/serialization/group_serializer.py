from rest_framework import serializers

class GroupSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(read_only=True)

    number_of_subgroups = serializers.IntegerField(read_only=True)