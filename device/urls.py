from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.DeviceCreateView.as_view()),
    path('',views.DeviceListView.as_view()),
    path('<int:pk>/',views.DeviceDetailView.as_view()),
]