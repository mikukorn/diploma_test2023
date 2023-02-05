from django.urls import path

from .views import list_results, healthcheck

app_name = 'api'

urlpatterns = [
    path("hooks/handler_results", list_results),
    path("hooks/get_status", healthcheck)
]