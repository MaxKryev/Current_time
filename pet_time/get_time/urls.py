from django.urls import path
from .views import RemoteTimeView

urlpatterns = [
    path('remote_time/', RemoteTimeView.as_view(), name='remote_time'),
]
