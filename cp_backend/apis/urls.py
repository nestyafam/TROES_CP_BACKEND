from django.urls import path
from .views import *

app_name = 'apis'

urlpatterns = [
    path('micontrol/', ControlView.as_view(), name='control'),
]
