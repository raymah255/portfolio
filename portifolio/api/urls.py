from django.urls import path


from .views import (
    comment_list_views,
    feed_list_views,
    post_list_views,
    post_detail_views,
    create_comment_views,
    post_like_views,
    post_create_view,
    notifacation_views,
    create_post_notifacation_views
)

urlpatterns = [
    path('posts/', post_list_views),
    path('feeds/', feed_list_views),
    path('comments/', comment_list_views),
    path('post/create/', post_create_view),
    path('post/like/', post_like_views),
    path('posts/<slug:slug>/', post_detail_views),
    path('comments/create/', create_comment_views),
    path('notification/', notifacation_views),
    path('notification/post/create/', create_post_notifacation_views), 
]