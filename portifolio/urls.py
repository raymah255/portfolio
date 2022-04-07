from turtle import home
from django.urls import path
from .views import(
    blog_detail_views,
    blog_home,
    create_comment_views,
    home_views,
    post_list_views,
    post_detail_views,
    blog_feeds_home,
)


urlpatterns = [
    path('', home_views),
    path('blog/', blog_home),
    path('feeds/', blog_feeds_home),
    path('posts/', post_list_views),
    path('blog/<slug:slug>/', blog_detail_views),
    path('posts/<slug:slug>/', post_detail_views),
    path('comment/create/', create_comment_views),
]
