from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')


    class Meta:
        model = Post
        fields = ('url', 'id', 'author','title', 'text', 'created_date', 'comment_set', )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)


    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts',)

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('url', 'id', 'author', 'text', 'post',)

