app_name = 'forum'

from django.urls import path, include
from . import views


urlpatterns = [
    path('NOUSE', views.lool),

]