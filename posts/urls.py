from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Blog API')


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root, name='api-root'),
    path('schema/', schema_view),
    path('charts/', views.ChartData.as_view(), name='chart-list'),
    path('charts/line/', views.ChartDataLine.as_view(), name='line-chart'),
    path('charts/bar/', views.ChartDataBar.as_view(), name='bar-chart'),
]
urlpatterns = format_suffix_patterns(urlpatterns)