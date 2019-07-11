from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'text',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    depth = 2
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text', 'created_date', 'comments',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)


    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts',)

