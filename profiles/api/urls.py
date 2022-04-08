from django.urls import path
from .views import profile_views, user_profile_views, user_profile_search_views


urlpatterns = [
    path('', user_profile_views),
    path('search/', user_profile_search_views),
    path('<str:username>/', profile_views),
]
