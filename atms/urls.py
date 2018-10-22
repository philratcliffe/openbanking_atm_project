from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='atms-views-list'),
    path('list/', views.list, name='atms-views-list'),
    path('map/', views.map, name='atms-views-map'),
]
