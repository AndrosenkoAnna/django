from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
