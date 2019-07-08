from django.shortcuts import render, render_to_response
from rest_framework import viewsets
from .models import Post, Comment
from rest_framework import generics, permissions, renderers
from .serializers import PostSerializer, UserSerializer, CommentSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from bokeh.plotting import figure, show
from bokeh.embed import components

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny, )

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format),
        'charts': reverse('chart-list', request=request, format=format)
    })

class ChartDataLine(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []


    def get(self, request, format=None):
        x = [1, 2, 3, 4, 5]
        y = [9, 15, 10, 13, 19]
        plot = figure(title='Line Graph', x_axis_label ='X-Axis', y_axis_label = 'Y-Axis', plot_width = 400, plot_height = 400)
        plot.line(x, y, color="navy")
        script, div = components(plot)
        return render_to_response('posts/base.html', {'script': script, 'div': div})

class ChartDataBar(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, format=None):
        x = [10, 20, 15, 13, 19]
        y = [a**2 for a in x]

        plot = figure(title="Bar Graph", plot_height = 400)

        plot.vbar(x, width = 0.5, bottom = 0, top = y, color = 'firebrick')

        script, div = components(plot)
        return render_to_response('posts/base.html', {'script': script, 'div': div})

class ChartData(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render_to_response('posts/base.html')

