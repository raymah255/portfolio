from django.urls import path
from .views import profile_views, my_profile_views


urlpatterns = [    
    path('<str:username>', my_profile_views),
    path('edit/<str:username>', profile_views),
]
