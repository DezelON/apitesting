from rest_framework import serializers

class AppSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    api = serializers.CharField(max_length=20)
    dateofcreation = serializers.IntegerField(default=0)
    description = serializers.CharField(max_length=500)