import logging

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

logger = logging.getLogger(__name__)
logger.info(settings.RUN_TYPE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
]
