import logging

from django.conf import settings
from django.contrib import admin
from django.urls import path

logger = logging.getLogger(__name__)
logger.info(settings.RUN_TYPE)
logger.debug('Debugging is enabled.')
logger.info('Debug mode is active.')

urlpatterns = [
    path('admin/', admin.site.urls),
]
