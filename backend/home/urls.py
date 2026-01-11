from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_logged, name='home_logged'),
    path('not-logged', views.home_not_logged, name='home_not_logged'),
]
