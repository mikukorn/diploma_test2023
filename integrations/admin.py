from django.contrib import admin
from .models import *


class TestRunAdmin(admin.ModelAdmin):
    pass

class TestRunResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'body_test', 'created')
    empty_value_display = '-пусто-'


class DroneCIListResultsAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


admin.site.register(TestRunResults, TestRunResultsAdmin)
admin.site.register(DroneCIListResults, DroneCIListResultsAdmin)

