from rest_framework import serializers
from post.models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['pk', 'user', 'name', 'image']


class PostSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Post
        fields = ('pk', 'isDraft', 'name', 'body', 'publication_date')