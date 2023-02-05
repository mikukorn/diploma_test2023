from django.urls import path
from . import views
from .views import *

app_name = 'test-runs'

urlpatterns = [
    path('', DroneCIRunListIndex.as_view(), name='all_runs'),
]