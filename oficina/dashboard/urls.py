from django.urls import path
from .views import dashboard

urlpatterns = [
    path('', view=dashboard, name='dashboard'),
]
