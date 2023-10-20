from django.urls import path
from .views import CurrentTimeView

urlpatterns = [
    path('current_time/', CurrentTimeView.get, name='current_time'),
]
