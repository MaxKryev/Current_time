import requests
from django.http import JsonResponse
from django.utils.timezone import localtime
from rest_framework.views import APIView

# Create your views here.


class CurrentTimeView(APIView):
    def get(self, request):
        response = requests.get('http://worldtimeapi.org/api/ip')
        if response.status_code == 200:
            current_time = response.json()['current_time']
            return JsonResponse({"current_time": current_time})
        else:
            return JsonResponse({"error": "Failed to get the current time from the API"}, status=500)
