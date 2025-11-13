from rest_framework import serializers

from blog.choices import CATEGORY_CHOICES


class BlogPostSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    is_active = serializers.BooleanField(default=True)
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)



