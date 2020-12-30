from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/objectives', include('objectives.urls')),
    path('api/v1/users', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
