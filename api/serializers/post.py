from rest_framework import serializers
from ..models.post import Post
from .user import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    # author = serializers.ReadOnlyField(source='author.id')
    class Meta:
        model = Post
        fields = ('id', 'title', 'location', 'content', 'created_at', 'author', 'image')



class PostPostSerializer(serializers.ModelSerializer):
     class Meta:
        model = Post
        fields = ('id', 'title', 'location', 'content', 'created_at', 'author', 'image')

class UpdatePostSerializer(serializers.ModelSerializer):
     class Meta:
        model = Post
        fields = ('id', 'title', 'location', 'content', 'created_at', 'author', 'image')