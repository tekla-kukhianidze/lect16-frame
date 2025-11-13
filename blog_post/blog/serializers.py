# from rest_framework import serializers
#
# from blog.choices import CATEGORY_CHOICES
#
#
# class BlogPostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=200)
#     text = serializers.CharField()
#     is_active = serializers.BooleanField(default=True)
#     category = serializers.ChoiceField(choices=CATEGORY_CHOICES)

from rest_framework import serializers

from blog.choices import CATEGORY_CHOICES
from blog.models import BlogPost, BlogPostCover


class BlogPostListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=200)
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)


class BlogPostDetailUpdateCreateSerializer(BlogPostListSerializer):
    text = serializers.CharField()
    is_active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        blog_post = BlogPost.objects.create(**self.validated_data)
        return blog_post

class BlogPostSerializer(serializers.ModelSerializer):
    cover_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'category', 'text', 'is_active', 'cover_image']


    def create(self, validated_data):
        cover_image = validated_data.pop('cover_image')
        blog_post = BlogPost.objects.create(**validated_data)
        BlogPostCover.objects.create(blog_post=blog_post, image=cover_image)
        return blog_post

