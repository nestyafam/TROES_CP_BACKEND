from django.urls import path
from .views import *

app_name = 'apis'

urlpatterns = [
    path('micontrol/', MiControlView.as_view(), name='micontrol'),
]
