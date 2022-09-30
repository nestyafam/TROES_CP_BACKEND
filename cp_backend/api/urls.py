from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('micontrol/', ControlView.as_view(), name='control'),
]
