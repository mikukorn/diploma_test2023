from django.urls import path
from . import views
from .views import TestsFeature

app_name = 'tests'

urlpatterns = [
    path('', views.ListIndex.as_view(), name='index'),
    path('add_scenario/', views.CreateScenario.as_view(), name='add_scenario'),
    path('add_feature/', views.CreateFeature.as_view(), name='add_feature'),
    path('test/<int:pk>/', views.DetailScenario.as_view(), name='get_scenario'),
    path('test/update/<int:pk>/', views.UpdateScenario.as_view(), name='update_scenario'),
    path('test/update/<int:pk>/', views.DeleteScenario.as_view(), name='delete_scenario'),
    path('tests/', views.ListAllScenario.as_view(), name='all_scenario'),
    path('tests/<slug:feature_slug>/', TestsFeature.as_view(), name='feature_list'),
    path('test/<int:pk>/comment/', views.DetailScenario.as_view(), name='add_comment'),

]