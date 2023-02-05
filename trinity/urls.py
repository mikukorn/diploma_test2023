from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tests.urls', namespace='tests')),
    path('api/', include('integrations.urls', namespace='api')),
    path('test-run/', include('testruns.urls', namespace='test-runs'))
]
