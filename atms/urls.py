from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='atms-views-list'),
    path('map/', views.map, name='atms-views-map'),
    path('list/', views.list, name='atms-views-list'),
    path('local_list/', views.ATMListView.as_view(), name='atms-views-local-list'),
]
