from django.contrib import admin
from .models import *


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'last_update_user', 'create_date', 'update_date',)
    list_filter = ('last_update_user',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'text', 'author', 'created', 'updated', 'scenario_public',)
    empty_value_display = '-пусто-'


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('level', 'name')
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(FeatureTest, FeaturesAdmin)
