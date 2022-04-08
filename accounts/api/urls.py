from django.urls import path
from .views import user_serilazers_views


urlpatterns = [
    path('', user_serilazers_views)
]
