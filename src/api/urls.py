from django.urls import path

from . import views

urlpatterns = [
    path('devices/', views.DeviceCreateAPIView.as_view()),
    path('devices/<str:order_id>/', views.DeviceRetrieveAPIView.as_view()),
]
