from django.urls import path
from .views import load_message_views, create_message_views

urlpatterns = [    
    path('create/', create_message_views),
    path('<username>/', load_message_views),

]
