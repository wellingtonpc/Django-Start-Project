from django.conf import settings

from django.contrib import admin
from django.urls import path

print(settings.RUN_TYPE)
urlpatterns = [
    path('admin/', admin.site.urls),
]
