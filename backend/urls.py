from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portifolio.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('portifolio.api.urls')),
    path('api/profile/', include('profiles.api.urls')),
    path("profile/", include("profiles.urls")),
    path("chat/", include("chat.urls")),
    path("api/chat/", include("chat.api.urls")),
    path("api/accounts/", include("accounts.api.urls")),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


