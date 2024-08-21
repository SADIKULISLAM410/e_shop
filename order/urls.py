from . import views
from django.urls import path

urlpatterns = [
    path('', views.order, name = 'order'),
]