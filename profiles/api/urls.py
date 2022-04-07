from django.urls import path
from .views import profile_views


urlpatterns = [
    path('<str:username>/', profile_views),
]
